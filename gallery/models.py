from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Cottage Rules
    corporate_allowed = models.BooleanField(default=True)
    alcohol_allowed = models.BooleanField(default=True)
    pets_allowed = models.BooleanField(default=True)
    zags_allowed = models.BooleanField(default=True)
    marriage_certificate_required = models.BooleanField(default=False)

    # Schedule
    check_in_time = models.CharField(max_length=10, default='19:00')
    check_out_time = models.CharField(max_length=10, default='17:00')
    quiet_hours_start = models.CharField(max_length=10, default='22:00')
    quiet_hours_end = models.CharField(max_length=10, default='07:00')

    # Capacity
    max_guests = models.IntegerField(default=12)
    bedrooms = models.IntegerField(default=4)
    beds = models.IntegerField(default=12)

    # Amenities
    has_playstation = models.BooleanField(default=False)
    has_karaoke = models.BooleanField(default=False)
    has_hammam = models.BooleanField(default=False)
    has_table_tennis = models.BooleanField(default=False)
    has_billiards = models.BooleanField(default=False)
    has_outdoor_pool = models.BooleanField(default=False)
    has_hookah = models.BooleanField(default=False)
    has_jacuzzi = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    has_summer_kitchen = models.BooleanField(default=False)
    has_barbecue = models.BooleanField(default=False)
    has_mangal = models.BooleanField(default=False)

    # Pool dimensions
    pool_length = models.IntegerField(blank=True, null=True)
    pool_width = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='blogs/')
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
