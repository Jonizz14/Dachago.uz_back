from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Blog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'title', 'photo', 'price', 'description', 'created_at',
            # Rules
            'corporate_allowed', 'alcohol_allowed', 'pets_allowed',
            'zags_allowed', 'marriage_certificate_required',
            # Schedule
            'check_in_time', 'check_out_time', 'quiet_hours_start', 'quiet_hours_end',
            # Capacity
            'max_guests', 'bedrooms', 'beds',
            # Amenities
            'has_playstation', 'has_karaoke', 'has_hammam', 'has_table_tennis',
            'has_billiards', 'has_outdoor_pool', 'has_hookah', 'has_jacuzzi',
            'has_wifi', 'has_summer_kitchen', 'has_barbecue', 'has_mangal',
            # Pool
            'pool_length', 'pool_width',
        ]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'photo', 'description', 'published_date']
