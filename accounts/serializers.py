from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ValidationError

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
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
                # Let it pass, SimpleJWT will handle invalid credentials
                pass

        return super().validate(attrs)
