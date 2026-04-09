from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Product, ProductImage, Blog, Contact, Booking, Review, Activity,
    Employee, Payment, Service, Announcement, AnnouncementImage, Settings
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    locationLat = serializers.CharField(source='latitude', allow_null=True, required=False)
    locationLon = serializers.CharField(source='longitude', allow_null=True, required=False)
    location = serializers.CharField(source='location_name', allow_null=True, required=False)
    busy_dates = serializers.SerializerMethodField()
    amenities = serializers.SerializerMethodField()
    images = ProductImageSerializer(many=True, read_only=True)
    rating = serializers.FloatField()
    bookings_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'category', 'status',
            # Basic Info
            'title_ru', 'title_uz', 'title_en',
            'description_ru', 'description_uz', 'description_en',
            'photo', 'price', 'created_at',
            
            # Location
            'locationLat', 'locationLon', 'location',
            'busy_dates', 'amenities',
            
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
            'max_guests', 'bedrooms', 'bathrooms', 'floors', 'total_area', 'land_area', 'parking_places',
            'beds', 'beds_ru', 'beds_uz', 'beds_en',
            
            # Amenities booleans
            'has_tapchan', 'has_fireplace', 'has_playstation', 'has_karaoke', 'has_tv', 'has_computer',
            'has_kitchen', 'has_microwave', 'has_refrigerator', 'has_gas_stove', 'has_summer_kitchen',
            'has_barbecue', 'has_mangal', 'has_sauna', 'has_salt_room', 'has_hammam', 'has_jacuzzi',
            'has_indoor_pool', 'has_outdoor_pool', 'has_washing_machine', 'has_iron',
            'has_table_tennis', 'has_billiards', 'has_chess', 'has_hookah', 'has_wifi',

            # Amenity details
            'sauna_daily_limit_hours', 'sauna_rule_ru', 'sauna_rule_uz', 'sauna_rule_en',
            'indoor_pool_length', 'indoor_pool_width', 'indoor_pool_heated',
            'outdoor_pool_length', 'outdoor_pool_width',
            'rating', 'bookings_count', 'images',
        ]

    def get_bookings_count(self, obj):
        return obj.bookings.count()

    def get_busy_dates(self, obj):
        return obj.availability.filter(is_busy=True).values_list('date', flat=True)

    def get_amenities(self, obj):
        labels = {
            'has_tapchan': {'ru': 'Тапчан', 'uz': 'Tapchan', 'en': 'Tapchan'},
            'has_fireplace': {'ru': 'Камин', 'uz': 'Kamin', 'en': 'Fireplace'},
            'has_playstation': {'ru': 'PlayStation', 'uz': 'PlayStation', 'en': 'PlayStation'},
            'has_karaoke': {'ru': 'Караоке', 'uz': 'Karaoke', 'en': 'Karaoke'},
            'has_tv': {'ru': 'Телевизор', 'uz': 'Televizor', 'en': 'TV'},
            'has_computer': {'ru': 'Компьютер', 'uz': 'Kompyuter', 'en': 'Computer'},
            'has_kitchen': {'ru': 'Кухня', 'uz': 'Oshxona', 'en': 'Kitchen'},
            'has_microwave': {'ru': 'Микроволновая печь', 'uz': "Mikroto'lqin pech", 'en': 'Microwave'},
            'has_refrigerator': {'ru': 'Холодильник', 'uz': 'Muzlatgich', 'en': 'Refrigerator'},
            'has_gas_stove': {'ru': 'Газовая плита', 'uz': 'Gaz plita', 'en': 'Gas Stove'},
            'has_summer_kitchen': {'ru': 'Летняя кухня', 'uz': 'Yozgi oshxona', 'en': 'Summer Kitchen'},
            'has_barbecue': {'ru': 'Барбекю', 'uz': 'Barbekyu', 'en': 'Barbecue'},
            'has_mangal': {'ru': 'Мангал', 'uz': 'Mangal', 'en': 'BBQ'},
            'has_sauna': {'ru': 'Финская сауна', 'uz': 'Fin saunasi', 'en': 'Finnish Sauna'},
            'has_salt_room': {'ru': 'Соляная комната', 'uz': 'Tuz xonasi', 'en': 'Salt Room'},
            'has_hammam': {'ru': 'Турецкий хаммам', 'uz': 'Turk hammomi', 'en': 'Turkish Hammam'},
            'has_jacuzzi': {'ru': 'Джакузи', 'uz': 'Jakuzi', 'en': 'Jacuzzi'},
            'has_indoor_pool': {'ru': 'Крытый бассейн', 'uz': 'Yopiq basseyn', 'en': 'Indoor Pool'},
            'has_outdoor_pool': {'ru': 'Открытый бассейн', 'uz': 'Ochiq basseyn', 'en': 'Outdoor Pool'},
            'has_washing_machine': {'ru': 'Стиральная машина', 'uz': 'Kir yuvish mashinasi', 'en': 'Washing Machine'},
            'has_iron': {'ru': 'Утюг', 'uz': 'Dazmol', 'en': 'Iron'},
            'has_table_tennis': {'ru': 'Настольный теннис', 'uz': 'Stol tennisi', 'en': 'Table Tennis'},
            'has_billiards': {'ru': 'Бильярд', 'uz': 'Bilyard', 'en': 'Billiards'},
            'has_chess': {'ru': 'Шахматы', 'uz': 'Shaxmat', 'en': 'Chess'},
            'has_hookah': {'ru': 'Кальян', 'uz': 'Kalyan', 'en': 'Hookah'},
            'has_wifi': {'ru': 'WI-FI', 'uz': 'WI-FI', 'en': 'WI-FI'},
        }
        
        result = []
        for field, names in labels.items():
            if getattr(obj, field, False):
                result.append({
                    'slug': field.replace('has_', ''),
                    'name_ru': names['ru'],
                    'name_uz': names['uz'],
                    'name_en': names['en']
                })
        return result


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id',
            'title_ru', 'title_uz', 'title_en',
            'description_ru', 'description_uz', 'description_en',
            'photo', 'published_date'
        ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id', 'name', 'email', 'phone', 'subject', 'message',
            'created_at', 'is_read', 'status'
        ]
        read_only_fields = ['created_at', 'is_read', 'status']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'user_name', 'rating', 'comment', 'status', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class AnnouncementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementImage
        fields = ['id', 'image', 'created_at']


class AnnouncementSerializer(serializers.ModelSerializer):
    images = AnnouncementImageSerializer(many=True, read_only=True)

    class Meta:
        model = Announcement
        fields = [
            'id', 'title', 'content', 'photo', 'date', 
            'status', 'views', 'created_at', 'images'
        ]


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'
