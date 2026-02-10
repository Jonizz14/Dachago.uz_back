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
            'id',
            # Basic Info (multilingual)
            'title_ru', 'title_uz', 'title_en',
            'description_ru', 'description_uz', 'description_en',
            'photo', 'price', 'created_at',
            
            # Cottage Rules
            'corporate_allowed', 'corporate_rule_ru', 'corporate_rule_uz', 'corporate_rule_en',
            'alcohol_allowed', 'alcohol_rule_ru', 'alcohol_rule_uz', 'alcohol_rule_en',
            'pets_allowed', 'pets_rule_ru', 'pets_rule_uz', 'pets_rule_en',
            'zags_allowed', 'zags_rule_ru', 'zags_rule_uz', 'zags_rule_en',
            'marriage_certificate_required', 'marriage_rule_ru', 'marriage_rule_uz', 'marriage_rule_en',
            
            # Schedule
            'check_in_time', 'check_in_rule_ru', 'check_in_rule_uz', 'check_in_rule_en',
            'check_out_time', 'check_out_rule_ru', 'check_out_rule_uz', 'check_out_rule_en',
            'quiet_hours_start', 'quiet_hours_end', 'quiet_hours_rule_ru', 'quiet_hours_rule_uz', 'quiet_hours_rule_en',
            
            # Capacity
            'max_guests', 'guests_ru', 'guests_uz', 'guests_en',
            'bedrooms', 'bedrooms_ru', 'bedrooms_uz', 'bedrooms_en',
            'beds', 'beds_ru', 'beds_uz', 'beds_en',
            
            # Media & Technologies
            'has_playstation', 'playstation_ru', 'playstation_uz', 'playstation_en',
            'has_karaoke', 'karaoke_ru', 'karaoke_uz', 'karaoke_en',
            'has_tv', 'tv_ru', 'tv_uz', 'tv_en',
            'has_computer', 'computer_ru', 'computer_uz', 'computer_en',
            
            # Kitchen
            'has_kitchen', 'kitchen_ru', 'kitchen_uz', 'kitchen_en',
            'has_microwave', 'microwave_ru', 'microwave_uz', 'microwave_en',
            'has_refrigerator', 'refrigerator_ru', 'refrigerator_uz', 'refrigerator_en',
            'has_gas_stove', 'gas_stove_ru', 'gas_stove_uz', 'gas_stove_en',
            
            # Outdoor
            'has_summer_kitchen', 'summer_kitchen_ru', 'summer_kitchen_uz', 'summer_kitchen_en',
            'has_barbecue', 'barbecue_ru', 'barbecue_uz', 'barbecue_en',
            'has_mangal', 'mangal_ru', 'mangal_uz', 'mangal_en',
            
            # Health & Wellness
            'has_sauna', 'sauna_ru', 'sauna_uz', 'sauna_en',
            'sauna_daily_limit_hours', 'sauna_rule_ru', 'sauna_rule_uz', 'sauna_rule_en',
            'has_salt_room', 'salt_room_ru', 'salt_room_uz', 'salt_room_en',
            'has_hammam', 'hammam_ru', 'hammam_uz', 'hammam_en',
            'has_jacuzzi', 'jacuzzi_ru', 'jacuzzi_uz', 'jacuzzi_en',
            
            # Pools
            'has_indoor_pool', 'indoor_pool_ru', 'indoor_pool_uz', 'indoor_pool_en',
            'indoor_pool_length', 'indoor_pool_width', 'indoor_pool_heated',
            'has_outdoor_pool', 'outdoor_pool_ru', 'outdoor_pool_uz', 'outdoor_pool_en',
            'outdoor_pool_length', 'outdoor_pool_width',
            
            # Cleaning Services
            'has_washing_machine', 'washing_machine_ru', 'washing_machine_uz', 'washing_machine_en',
            'has_iron', 'iron_ru', 'iron_uz', 'iron_en',
            
            # Sports & Recreation
            'has_table_tennis', 'table_tennis_ru', 'table_tennis_uz', 'table_tennis_en',
            'has_billiards', 'billiards_ru', 'billiards_uz', 'billiards_en',
            'has_chess', 'chess_ru', 'chess_uz', 'chess_en',
            'has_hookah', 'hookah_ru', 'hookah_uz', 'hookah_en',
            
            # Other
            'has_wifi', 'wifi_ru', 'wifi_uz', 'wifi_en',
        ]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id',
            'title_ru', 'title_uz', 'title_en',
            'description_ru', 'description_uz', 'description_en',
            'photo', 'published_date'
        ]
