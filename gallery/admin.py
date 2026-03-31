from django.contrib import admin
from .models import (
    Product, Blog, Contact, CottageAvailability, 
    Employee, Payment, Service, Announcement, Booking, Review, Activity, Settings
)


class AvailabilityInline(admin.TabularInline):
    model = CottageAvailability
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'price', 'category', 'status', 'max_guests', 'bedrooms', 'bathrooms', 'created_at')
    search_fields = ('title_ru', 'title_uz', 'title_en', 'location_name')
    list_filter = ('category', 'status', 'created_at', 'price', 'bedrooms', 'bathrooms', 'has_tapchan')
    inlines = [AvailabilityInline]
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('title_ru', 'title_uz', 'title_en', 'description_ru', 'description_uz', 'description_en', 'photo', 'price', 'category', 'status')
        }),
        ('Location', {
            'fields': ('latitude', 'longitude', 'location_name')
        }),
        ('Capacity & Area', {
            'fields': ('max_guests', 'bedrooms', 'bathrooms', 'floors', 'total_area', 'land_area', 'parking_places', 'beds', 'beds_ru', 'beds_uz', 'beds_en')
        }),
        ('Rules & Schedule', {
            'fields': (
                'corporate_allowed', 'corporate_rule_ru', 'corporate_rule_uz', 'corporate_rule_en',
                'alcohol_allowed', 'alcohol_rule_ru', 'alcohol_rule_uz', 'alcohol_rule_en',
                'pets_allowed', 'pets_rule_ru', 'pets_rule_uz', 'pets_rule_en',
                'zags_allowed', 'zags_rule_ru', 'zags_rule_uz', 'zags_rule_en',
                'marriage_certificate_required', 'marriage_rule_ru', 'marriage_rule_uz', 'marriage_rule_en',
                'check_in_time', 'check_in_rule_ru', 'check_in_rule_uz', 'check_in_rule_en',
                'check_out_time', 'check_out_rule_ru', 'check_out_rule_uz', 'check_out_rule_en',
                'quiet_hours_start', 'quiet_hours_end', 'quiet_hours_rule_ru', 'quiet_hours_rule_uz', 'quiet_hours_rule_en'
            )
        }),
        ('Amenities', {
            'fields': (
                'has_tapchan', 'has_fireplace', 'has_playstation', 'has_karaoke', 'has_tv', 'has_computer',
                'has_kitchen', 'has_microwave', 'has_refrigerator', 'has_gas_stove', 'has_summer_kitchen',
                'has_barbecue', 'has_mangal', 'has_sauna', 'sauna_daily_limit_hours', 'sauna_rule_ru', 'sauna_rule_uz', 'sauna_rule_en',
                'has_salt_room', 'has_hammam', 'has_jacuzzi', 'has_indoor_pool', 'indoor_pool_length', 'indoor_pool_width', 'indoor_pool_heated',
                'has_outdoor_pool', 'outdoor_pool_length', 'outdoor_pool_width', 'has_washing_machine', 'has_iron',
                'has_table_tennis', 'has_billiards', 'has_chess', 'has_hookah', 'has_wifi'
            )
        }),
    )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'published_date')
    search_fields = ('title_ru', 'title_uz', 'title_en')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at', 'is_read')
    search_fields = ('name', 'email', 'message')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ['-created_at']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'phone', 'status')
    list_filter = ('status', 'position')
    search_fields = ('name', 'email', 'phone')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'customer_name', 'cottage_name', 'amount', 'method', 'status', 'date')
    list_filter = ('status', 'method', 'date')
    search_fields = ('transaction_id', 'customer_name', 'cottage_name')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', 'status')
    list_filter = ('status',)
    search_fields = ('name',)


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'status', 'views')
    list_filter = ('status', 'date')
    search_fields = ('title', 'content')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('product', 'user_name', 'date', 'amount_display', 'status', 'created_at')
    list_filter = ('status', 'date', 'created_at')
    search_fields = ('product__title_ru', 'user_name', 'user__email')
    
    def amount_display(self, obj):
        return f"${obj.price}"
    amount_display.short_description = "Amount"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user_name', 'rating', 'status', 'created_at')
    list_filter = ('rating', 'status', 'created_at')
    search_fields = ('product__title_ru', 'user_name', 'comment')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_type', 'created_at')
    list_filter = ('icon_type', 'created_at')
    search_fields = ('title', 'description')


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'contact_email', 'contact_phone')


@admin.register(CottageAvailability)
class CottageAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('product', 'date', 'is_busy')
    list_filter = ('date', 'is_busy', 'product')
    search_fields = ('product__title_ru', 'product__title_uz', 'product__title_en')
