from django.db import models


class Product(models.Model):
    # Basic Info (multilingual)
    title_ru = models.CharField(max_length=255, blank=True, null=True)
    title_uz = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    
    description_ru = models.TextField(blank=True, null=True)
    description_uz = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    
    photo = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    # Categories & Status
    CATEGORY_CHOICES = (
        ('Amirsoy', 'Amirsoy'),
        ('Charvak', 'Charvak'),
        ('Chimgan', 'Chimgan'),
        ('Oqtosh', 'Oqtosh'),
        ('Parkent', 'Parkent'),
        ('Sijjak', 'Sijjak'),
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Cottage')
    
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)

    # Location Info
    latitude = models.CharField(max_length=50, blank=True, null=True, verbose_name="Latitude")
    longitude = models.CharField(max_length=50, blank=True, null=True, verbose_name="Longitude")
    location_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Location Name")

    # Cottage Rules (multilingual)
    corporate_allowed = models.BooleanField(default=True)
    corporate_rule_ru = models.TextField(blank=True, null=True, verbose_name="Корпоратив")
    corporate_rule_uz = models.TextField(blank=True, null=True, verbose_name="Korparativ")
    corporate_rule_en = models.TextField(blank=True, null=True, verbose_name="Corporate")
    
    alcohol_allowed = models.BooleanField(default=True)
    alcohol_rule_ru = models.TextField(blank=True, null=True, verbose_name="Алкоголь")
    alcohol_rule_uz = models.TextField(blank=True, null=True, verbose_name="Alkogol")
    alcohol_rule_en = models.TextField(blank=True, null=True, verbose_name="Alcohol")
    
    pets_allowed = models.BooleanField(default=True)
    pets_rule_ru = models.TextField(blank=True, null=True, verbose_name="Домашние животные")
    pets_rule_uz = models.TextField(blank=True, null=True, verbose_name="Uy hayvonlari")
    pets_rule_en = models.TextField(blank=True, null=True, verbose_name="Pets")
    
    zags_allowed = models.BooleanField(default=True)
    zags_rule_ru = models.TextField(blank=True, null=True, verbose_name="ЗАГС")
    zags_rule_uz = models.TextField(blank=True, null=True, verbose_name="ROG")
    zags_rule_en = models.TextField(blank=True, null=True, verbose_name="Registry Office")
    
    marriage_certificate_required = models.BooleanField(default=False)
    marriage_rule_ru = models.TextField(blank=True, null=True, verbose_name="Свидетельство о браке")
    marriage_rule_uz = models.TextField(blank=True, null=True, verbose_name="Nikoh guvohnomasi")
    marriage_rule_en = models.TextField(blank=True, null=True, verbose_name="Marriage Certificate")

    # Schedule (multilingual)
    check_in_time = models.CharField(max_length=10, default='19:00')
    check_in_rule_ru = models.TextField(blank=True, null=True, verbose_name="Заезд")
    check_in_rule_uz = models.TextField(blank=True, null=True, verbose_name="Kirish")
    check_in_rule_en = models.TextField(blank=True, null=True, verbose_name="Check-in")
    
    check_out_time = models.CharField(max_length=10, default='17:00')
    check_out_rule_ru = models.TextField(blank=True, null=True, verbose_name="Выезд")
    check_out_rule_uz = models.TextField(blank=True, null=True, verbose_name="Chiqish")
    check_out_rule_en = models.TextField(blank=True, null=True, verbose_name="Check-out")
    
    quiet_hours_start = models.CharField(max_length=10, default='22:00')
    quiet_hours_end = models.CharField(max_length=10, default='07:00')
    quiet_hours_rule_ru = models.TextField(blank=True, null=True, verbose_name="Тихие часы")
    quiet_hours_rule_uz = models.TextField(blank=True, null=True, verbose_name="Tinch soatlar")
    quiet_hours_rule_en = models.TextField(blank=True, null=True, verbose_name="Quiet Hours")

    # Capacity
    max_guests = models.IntegerField(default=12, verbose_name="Макс. гостей")
    bedrooms = models.IntegerField(default=4, verbose_name="Спальни")
    bathrooms = models.IntegerField(default=1, verbose_name="Санузлы")
    floors = models.IntegerField(default=1, verbose_name="Этажность")
    total_area = models.IntegerField(default=0, verbose_name="Площадь дома (м²)")
    land_area = models.DecimalField(max_digits=5, decimal_places=1, default=0, verbose_name="Площадь участка (соток)")
    parking_places = models.IntegerField(default=0, verbose_name="Парковочных мест")

    beds = models.TextField(blank=True, null=True, verbose_name="Кровати")
    beds_ru = models.TextField(blank=True, null=True)
    beds_uz = models.TextField(blank=True, null=True, verbose_name="Karavotlar")
    beds_en = models.TextField(blank=True, null=True, verbose_name="Beds")

    # Amenities (additional)
    has_tapchan = models.BooleanField(default=False, verbose_name="Тапчан")
    has_fireplace = models.BooleanField(default=False, verbose_name="Камин")

    # Media & Technologies
    has_playstation = models.BooleanField(default=False, verbose_name="PlayStation")
    has_karaoke = models.BooleanField(default=False, verbose_name="Karaoke")
    has_tv = models.BooleanField(default=False, verbose_name="TV")
    has_computer = models.BooleanField(default=False, verbose_name="Computer")

    # Kitchen
    has_kitchen = models.BooleanField(default=False, verbose_name="Kitchen")
    has_microwave = models.BooleanField(default=False, verbose_name="Microwave")
    has_refrigerator = models.BooleanField(default=False, verbose_name="Refrigerator")
    has_gas_stove = models.BooleanField(default=False, verbose_name="Gas Stove")

    # Outdoor
    has_summer_kitchen = models.BooleanField(default=False, verbose_name="Summer Kitchen")
    has_barbecue = models.BooleanField(default=False, verbose_name="Barbecue")
    has_mangal = models.BooleanField(default=False, verbose_name="BBQ")

    # Health & Wellness
    has_sauna = models.BooleanField(default=False, verbose_name="Sauna")
    sauna_daily_limit_hours = models.IntegerField(blank=True, null=True, verbose_name="Sauna Daily Limit (Hours)")
    sauna_rule_ru = models.TextField(blank=True, null=True, verbose_name="Правила сауны (RU)")
    sauna_rule_uz = models.TextField(blank=True, null=True, verbose_name="Sauna qoidalari (UZ)")
    sauna_rule_en = models.TextField(blank=True, null=True, verbose_name="Sauna rules (EN)")
    
    has_salt_room = models.BooleanField(default=False, verbose_name="Salt Room")
    has_hammam = models.BooleanField(default=False, verbose_name="Hammam")
    has_jacuzzi = models.BooleanField(default=False, verbose_name="Jacuzzi")

    # Pools
    has_indoor_pool = models.BooleanField(default=False, verbose_name="Indoor Pool")
    indoor_pool_length = models.IntegerField(blank=True, null=True, verbose_name="Indoor Pool Length")
    indoor_pool_width = models.IntegerField(blank=True, null=True, verbose_name="Indoor Pool Width")
    indoor_pool_heated = models.BooleanField(default=False, verbose_name="Indoor Pool Heated")
    
    has_outdoor_pool = models.BooleanField(default=False, verbose_name="Outdoor Pool")
    outdoor_pool_length = models.IntegerField(blank=True, null=True, verbose_name="Outdoor Pool Length")
    outdoor_pool_width = models.IntegerField(blank=True, null=True, verbose_name="Outdoor Pool Width")

    # Cleaning Services
    has_washing_machine = models.BooleanField(default=False, verbose_name="Washing Machine")
    has_iron = models.BooleanField(default=False, verbose_name="Iron")

    # Sports & Recreation
    has_table_tennis = models.BooleanField(default=False, verbose_name="Table Tennis")
    has_billiards = models.BooleanField(default=False, verbose_name="Billiards")
    has_chess = models.BooleanField(default=False, verbose_name="Chess")
    has_hookah = models.BooleanField(default=False, verbose_name="Hookah")

    # Other
    has_wifi = models.BooleanField(default=False, verbose_name="Wi-Fi")

    def __str__(self):
        return self.title_ru or self.title_uz or self.title_en or "Product"
    
    @property
    def title(self):
        return self.title_ru or self.title_uz or self.title_en
    
    @property
    def description(self):
        return self.description_ru or self.description_uz or self.description_en


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.product.title}"


class Blog(models.Model):
    title_ru = models.CharField(max_length=255, blank=True, null=True)
    title_uz = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    
    description_ru = models.TextField(blank=True, null=True)
    description_uz = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    
    photo = models.ImageField(upload_to='blogs/')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_ru


class Contact(models.Model):
    """Model for storing contact form submissions"""
    name = models.CharField(max_length=255, verbose_name="Имя / Ism")
    email = models.EmailField(verbose_name="Email / Pochta")
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name="Телефон / Telefon")
    subject = models.CharField(max_length=255, blank=True, null=True, verbose_name="Тема / Mavzu")
    message = models.TextField(verbose_name="Сообщение / Xabar")
    
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, verbose_name="Прочитано / O'qilgan")
    
    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    
    class Meta:
        verbose_name = "Contact / Bog'lanish"
        verbose_name_plural = "Contacts / Bog'lanishlar"
        ordering = ['-created_at']


class CottageAvailability(models.Model):
    product = models.ForeignKey(Product, related_name='availability', on_delete=models.CASCADE)
    date = models.DateField()
    is_busy = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Cottage Availability / Bron qilingan kunlar"
        verbose_name_plural = "Cottages Availability / Bron qilingan kunlar"
        unique_together = ('product', 'date')
        ordering = ['date']

    def __str__(self):
        return f"{self.product.title} - {self.date} ({'Band' if self.is_busy else 'Bo`sh'})"


class Booking(models.Model):
    STATUS_CHOICES = (
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
    )
    
    product = models.ForeignKey(Product, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='bookings', on_delete=models.CASCADE, null=True, blank=True)
    user_name = models.CharField(max_length=255, help_text="Guest name if user is not registered")
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.product.title} - {self.user_name} ({self.status})"


class Review(models.Model):
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
    )
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='reviews', on_delete=models.CASCADE, null=True, blank=True)
    user_name = models.CharField(max_length=255)
    rating = models.IntegerField(default=5)
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='approved')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.product.title} - {self.rating} stars"


class Activity(models.Model):
    ICON_CHOICES = (
        ('user', 'User'),
        ('shopping', 'Shopping'),
        ('message', 'Message'),
        ('dollar', 'Dollar'),
        ('calendar', 'Calendar'),
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon_type = models.CharField(max_length=20, choices=ICON_CHOICES, default='user')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Activities"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Employee(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    transaction_id = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=255)
    cottage_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    method = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_id} - {self.amount}"


class Service(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    duration = models.CharField(max_length=100, help_text="e.g. Per Day, Per Hour")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('expired', 'Expired'),
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='announcements/', blank=True, null=True)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AnnouncementImage(models.Model):
    announcement = models.ForeignKey(Announcement, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='announcement_gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.announcement.title}"


class Settings(models.Model):
    site_name = models.CharField(max_length=255, default='DachaGo')
    contact_email = models.EmailField(default='info@dachago.uz')
    contact_phone = models.CharField(max_length=50, default='+998 90 123-45-67')
    default_language = models.CharField(max_length=10, default='uz')
    address = models.TextField(default='Tashkent, Uzbekistan')
    site_description = models.TextField(default='Find your perfect dacha in Uzbekistan')
    
    # Social Media
    telegram_link = models.URLField(blank=True, null=True, default='https://t.me/dachago')
    instagram_link = models.URLField(blank=True, null=True, default='https://instagram.com/dachago')
    facebook_link = models.URLField(blank=True, null=True, default='https://facebook.com/dachago')
    youtube_link = models.URLField(blank=True, null=True, default='https://youtube.com/dachago')
    
    # Notifications
    email_notifications = models.BooleanField(default=True)
    booking_notifications = models.BooleanField(default=True)
    review_notifications = models.BooleanField(default=True)
    payment_notifications = models.BooleanField(default=True)
    newsletter = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Settings"

    def __str__(self):
        return "Global Settings"
