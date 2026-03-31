import random
from datetime import date, timedelta
from django.db import migrations

def populate_location_and_availability(apps, schema_editor):
    Product = apps.get_model('gallery', 'Product')
    CottageAvailability = apps.get_model('gallery', 'CottageAvailability')
    
    locations = [
        {"name": "Amirsoy, Toshkent", "lat": "41.3111", "lon": "69.2797"},
        {"name": "Chorvoq, Toshkent viloyati", "lat": "41.6212", "lon": "70.0150"},
        {"name": "Chimyon, Bo'stonliq", "lat": "41.5458", "lon": "69.9702"},
        {"name": "Beldersoy, Toshkent viloyati", "lat": "41.4897", "lon": "69.9678"},
        {"name": "Humsan, Bo'stonliq", "lat": "41.1714", "lon": "69.8322"},
        {"name": "Bochka, Bo'stonliq", "lat": "41.5273", "lon": "69.8765"},
        {"name": "Nazarbek, Toshkent", "lat": "41.3508", "lon": "69.1354"},
    ]
    
    products = Product.objects.all()
    for product in products:
        loc = random.choice(locations)
        product.location_name = loc['name']
        product.latitude = loc['lat']
        product.longitude = loc['lon']
        product.save()
        
        # Add some busy dates for next 30 days
        today = date.today()
        for i in range(1, 15):
            if random.random() < 0.4: # 40% chance of being busy
                CottageAvailability.objects.get_or_create(
                    product=product,
                    date=today + timedelta(days=i),
                    defaults={'is_busy': True}
                )

class Migration(migrations.Migration):
    dependencies = [
        ('gallery', '0015_remove_product_barbecue_en_and_more'),
    ]
    operations = [
        migrations.RunPython(populate_location_and_availability),
    ]
