from django.db import migrations
from decimal import Decimal


def add_sample_data(apps, schema_editor):
    Product = apps.get_model('gallery', 'Product')
    Blog = apps.get_model('gallery', 'Blog')
    
    # Cottage 1: Dacha Go Premium
    Product.objects.create(
        title_ru="Загородный коттедж «Dacha Go»",
        title_uz="«Dacha Go» qishloq kotlaji",
        title_en="Country Cottage «Dacha Go»",
        description_ru="""В нашем коттедже есть все необходимые условия для отдыха с близкими.

ПРАВИЛА:
❌ Корпоративы запрещены
❌ Алкоголь запрещен
❌ Домашние животные запрещены
❌ ЗАГС запрещен

РАСПИСАНИЕ:
• Заезд: с 19:00
• Выезд: до 17:00

ВМЕСТИМОСТЬ:
• Гости: 15 человек
• Спальных комнат: 4

УДОБСТВА:
🎮 PlayStation | 🎤 Караоке | 🏊 Бассейн | 🧖 Сауна""",
        price=Decimal('1500000.00'),
        corporate_allowed=False,
        alcohol_allowed=False,
        pets_allowed=False,
        zags_allowed=False,
        marriage_certificate_required=False,
        check_in_time='19:00',
        check_out_time='17:00',
        quiet_hours_start='22:00',
        quiet_hours_end='07:00',
        max_guests=15,
        bedrooms=4,
        beds="15 односпальных, 1 двуспальная",
        has_playstation=True,
        has_karaoke=True,
        has_tv=True,
        has_computer=True,
        has_kitchen=True,
        has_microwave=True,
        has_refrigerator=True,
        has_gas_stove=True,
        has_summer_kitchen=True,
        has_barbecue=True,
        has_mangal=True,
        has_sauna=True,
        sauna_daily_limit_hours=3,
        has_salt_room=True,
        has_hammam=True,
        has_jacuzzi=True,
        has_indoor_pool=True,
        indoor_pool_length=8,
        indoor_pool_width=4,
        indoor_pool_heated=True,
        has_outdoor_pool=True,
        outdoor_pool_length=10,
        outdoor_pool_width=5,
        has_washing_machine=True,
        has_iron=True,
        has_table_tennis=True,
        has_billiards=True,
        has_chess=True,
        has_hookah=True,
        has_wifi=True,
    )
    
    # Cottage 2: Humsan Hills
    Product.objects.create(
        title_ru="Дача «Humsan Hills»",
        title_uz="«Humsan Hills» dam olish maskani",
        title_en="Cottage «Humsan Hills»",
        description_ru="Прекрасная дача для семейного отдыха вдали от городской суеты.",
        price=Decimal('1200000.00'),
        corporate_allowed=True,
        alcohol_allowed=True,
        pets_allowed=True,
        zags_allowed=True,
        check_in_time='14:00',
        check_out_time='12:00',
        quiet_hours_start='23:00',
        quiet_hours_end='08:00',
        max_guests=10,
        bedrooms=3,
        beds="8 односпальных, 1 двуспальная",
        has_karaoke=True,
        has_tv=True,
        has_kitchen=True,
        has_microwave=True,
        has_refrigerator=True,
        has_gas_stove=True,
        has_summer_kitchen=True,
        has_barbecue=True,
        has_mangal=True,
        has_hammam=True,
        has_jacuzzi=True,
        has_outdoor_pool=True,
        outdoor_pool_length=6,
        outdoor_pool_width=4,
        has_billiards=True,
        has_chess=True,
        has_hookah=True,
        has_wifi=True,
    )
    
    # Cottage 3: Halal Dacha
    Product.objects.create(
        title_ru="Халяль Дача",
        title_uz="Halal Dam Olish Maskani",
        title_en="Halal Cottage",
        description_ru="Отличная дача для семейного отдыха с соблюдением всех халяль традиций.",
        price=Decimal('1000000.00'),
        corporate_allowed=False,
        alcohol_allowed=False,
        pets_allowed=True,
        zags_allowed=True,
        check_in_time='12:00',
        check_out_time='11:00',
        quiet_hours_start='22:00',
        quiet_hours_end='07:00',
        max_guests=8,
        bedrooms=2,
        beds="6 односпальных, 1 двуспальная",
        has_kitchen=True,
        has_microwave=True,
        has_refrigerator=True,
        has_gas_stove=True,
        has_summer_kitchen=True,
        has_barbecue=True,
        has_mangal=True,
        has_outdoor_pool=True,
        outdoor_pool_length=5,
        outdoor_pool_width=3,
        has_chess=True,
        has_wifi=True,
    )
    
    # Cottage 4: Oilalar Uchun
    Product.objects.create(
        title_ru="Оила ва улфатларга",
        title_uz="Oila va Ulfatlar Uchun",
        title_en="Family and Friends",
        description_ru="Идеальное место для семей и друзей. Большой двор, мангал, качели для детей.",
        price=Decimal('800000.00'),
        corporate_allowed=True,
        alcohol_allowed=True,
        pets_allowed=True,
        zags_allowed=True,
        check_in_time='10:00',
        check_out_time='10:00',
        quiet_hours_start='23:00',
        quiet_hours_end='08:00',
        max_guests=12,
        bedrooms=3,
        beds="10 односпальных",
        has_kitchen=True,
        has_microwave=True,
        has_refrigerator=True,
        has_gas_stove=True,
        has_summer_kitchen=True,
        has_barbecue=True,
        has_mangal=True,
        has_outdoor_pool=True,
        outdoor_pool_length=6,
        outdoor_pool_width=3,
        has_wifi=True,
    )
    
    # Blog posts
    Blog.objects.create(
        title_ru="Отдых в загородном коттедже",
        title_uz="Qishloq koteljida dam olish",
        title_en="Country Cottage Vacation",
        description_ru="Отличный отдых вдали от городской суеты. Наш коттедж идеально подходит для семейного отдыха.",
        description_uz="Shahar shovqinidan uzoqda ajoyib dam olish.",
    )
    
    Blog.objects.create(
        title_ru="Турецкий хаммам и джакузи",
        title_uz="Turk hammomi va jakuzi",
        title_en="Turkish Hammam and Jacuzzi",
        description_ru="Расслабьтесь в нашем турецком хаммаме или насладитесь джакузи после долгого дня.",
        description_uz="Uzun kundan so'ng hammomda dam oling.",
    )
    
    Blog.objects.create(
        title_ru="Семейный отдых на природе",
        title_uz="Tabiatda oilaviy dam olish",
        title_en="Family Nature Vacation",
        description_ru="Отличная возможность провести время с семьёй на свежем воздухе.",
        description_uz="Oila bilan tabiatda vaqt o'tkazish.",
    )
    
    Blog.objects.create(
        title_ru="Бассейн и сауна",
        title_uz="Basseyn va sauna",
        title_en="Pool and Sauna",
        description_ru="Расслабьтесь в нашем бассейне и сауне. Идеальный отдых после рабочей недели.",
        description_uz="Basseyn va saunada dam oling. Ish haftasidan keyin ideal dam.",
        description_en="Relax in our pool and sauna. Perfect rest after work week.",
    )
    
    Blog.objects.create(
        title_ru="Караоке вечер",
        title_uz="Karaoke kechasi",
        title_en="Karaoke Night",
        description_ru="Устройте незабываемый караоке вечер с друзьями!",
        description_uz="Do'stlaringiz bilan esda qolmaydigan karaoke kechasi o'tkazing!",
        description_en="Have an unforgettable karaoke night with friends!",
    )
    
    Blog.objects.create(
        title_ru="Шашмаком и бильярд",
        title_uz="Shashmakom va bilyard",
        title_en="Chess and Billiards",
        description_ru="Играйте в шашмаком или бильярд с друзьями и семьёй.",
        description_uz="Do'stlaringiz va oilangiz bilan shashmakom va bilyard o'ynang.",
        description_en="Play chess or billiards with friends and family.",
    )
    
    Blog.objects.create(
        title_ru="Барбекю на природе",
        title_uz="Tabiatda barbekyu",
        title_en="BBQ in Nature",
        description_ru="Готовьте вкусный шашлык на мангале. Свежий воздух и аппетитная еда!",
        description_uz="Mangalda mazali shashlik pishiring. Tog' havo va mazali taomlar!",
        description_en="Cook delicious shashlik on the BBQ. Fresh air and tasty food!",
    )


def remove_sample_data(apps, schema_editor):
    Product = apps.get_model('gallery', 'Product')
    Blog = apps.get_model('gallery', 'Blog')
    Product.objects.filter(title_ru__startswith='Загородный коттедж').delete()
    Product.objects.filter(title_ru='Дача «Humsan Hills»').delete()
    Product.objects.filter(title_ru='Халяль Дача').delete()
    Product.objects.filter(title_ru='Оила ва улфатларга').delete()
    Blog.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_remove_blog_description_remove_blog_title_and_more'),
    ]

    operations = [
        migrations.RunPython(add_sample_data, remove_sample_data),
    ]
