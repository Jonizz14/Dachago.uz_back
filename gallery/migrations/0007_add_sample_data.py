from django.db import migrations
from django.utils import timezone
from decimal import Decimal


def create_cottage_product(apps, schema_editor):
    Product = apps.get_model('gallery', 'Product')
    Blog = apps.get_model('gallery', 'Blog')
    
    # Create cottage rental product
    cottage = Product.objects.create(
        title="Загородный коттедж «Dacha Go»",
        price=Decimal('1500000.00'),
        description="""В нашем коттедже есть все необходимые условия для отдыха с близкими.

ПРАВИЛА:
❌ Корпоративы запрещены
❌ Алкоголь запрещен
❌ Домашние животные запрещены
❌ ЗАГС запрещен

⚠️ Если семейные гости приезжают без детей, потребуется предъявить свидетельство о браке.

РАСПИСАНИЕ:
• Заезд: с 19:00
• Выезд: до 17:00
• Тихие часы: с 22:00 до 07:00

ВМЕСТИМОСТЬ:
• Гости: 12 человек
• Спальных комнат: 4
• Кровати: 12 односпальных

УДОБСТВА:
🎮 PlayStation | 🎤 Караоке | 🧖 Турецкий хаммам | 🏓 Настольный теннис
🎱 Бильярд | 🏊 Открытый бассейн 12x5м² | 🍃 Кальян

НА СВЕЖЕМ ВОЗДУХЕ:
🍖 Летняя кухня | 🍢 Барбекue | 🔥 Мангал

ОЗДОРОВИТЕЛЬНЫЕ:
🧖 Турецкий хаммам | 🛁 Джакузи

СПОРТ И ОТДЫХ:
🏓 Настольный теннис | 🎱 Бильярд | 🏊 Открытый бассейн 12x5м²

РАЗНОЕ:
📶 Wi-Fi | 🍃 Кальян""",
        created_at=timezone.now(),
        
        # Rules (all False = prohibited)
        corporate_allowed=False,
        alcohol_allowed=False,
        pets_allowed=False,
        zags_allowed=False,
        marriage_certificate_required=False,
        
        # Schedule
        check_in_time='19:00',
        check_out_time='17:00',
        quiet_hours_start='22:00',
        quiet_hours_end='07:00',
        
        # Capacity
        max_guests=12,
        bedrooms=4,
        beds=12,
        
        # Amenities
        has_playstation=True,
        has_karaoke=True,
        has_hammam=True,
        has_table_tennis=True,
        has_billiards=True,
        has_outdoor_pool=True,
        has_hookah=True,
        has_jacuzzi=True,
        has_wifi=True,
        has_summer_kitchen=True,
        has_barbecue=True,
        has_mangal=True,
        
        # Pool dimensions
        pool_length=12,
        pool_width=5,
    )
    
    # Create sample blog posts
    Blog.objects.create(
        title="Отдых в загородном коттедже",
        description="Отличный отдых вдали от городской суеты. Наш коттедж идеально подходит для семейного отдыха.",
    )
    
    Blog.objects.create(
        title="Турецкий хаммам и джакузи",
        description="Расслабьтесь в нашем турецком хаммаме или насладитесь джакузи после долгого дня.",
    )


def remove_cottage_product(apps, schema_editor):
    Product = apps.get_model('gallery', 'Product')
    Blog = apps.get_model('gallery', 'Blog')
    Product.objects.filter(title="Загородный коттедж «Dacha Go»").delete()
    Blog.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_remove_product_has_photo_alter_product_photo'),
    ]

    operations = [
        migrations.RunPython(create_cottage_product, remove_cottage_product),
    ]
