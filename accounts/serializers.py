from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, min_length=6, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, min_length=6, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm', 'first_name', 'last_name')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # We allow both username and email. 
        # TokenObtainPairSerializer by default uses username/password.
        # We will check if the input 'username' is actually an email.
        login_id = attrs.get('username')
        password = attrs.get('password')

        if '@' in login_id:
            try:
                user = User.objects.get(email=login_id)
                attrs['username'] = user.username
            except User.DoesNotExist:
                raise serializers.ValidationError("No user found with this email.")

        try:
            data = super().validate(attrs)
        except Exception as e:
            # Re-raise with a cleaner message if needed, or just let it pass
            raise e
        data['username'] = self.user.username
        data['email'] = self.user.email
        return data
