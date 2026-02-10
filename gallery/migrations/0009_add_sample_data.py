from django.db import migrations
from django.utils import timezone
from decimal import Decimal


def create_cottage_product(apps, schema_editor):
    Product = apps.get_model('gallery', 'Product')
    Blog = apps.get_model('gallery', 'Blog')
    
    # Create cottage rental product
    cottage = Product.objects.create(
        # Basic Info
        title_ru="Загородный коттедж «Dacha Go»",
        title_uz="«Dacha Go» qishloq kotlaji",
        title_en="Country Cottage «Dacha Go»",
        description_ru="""В нашем коттедже есть все необходимые условия для отдыха с близкими.

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
• Гости: 15 человек
• Спальных комнат: 4
• Кровати: 15 односпальных, 1 двуспальная

УДОБСТВА:
🎮 PlayStation | 🎤 Караоке | 🖥️ Компьютер | 🏓 Настольный теннис
🎱 Бильярд | 🏊 Крытый бассейн 8x4м² с подогревом | 🏊 Открытый бассейн 10х5м²
🍃 Кальян

НА СВЕЖЕМ ВОЗДУХЕ:
🍖 Летняя кухня | 🍢 Барбекю | 🔥 Мангал

ОЗДОРОВИТЕЛЬНЫЕ:
🧖 Финская сауна | 🛁 Джакузи | 🧖 Турецкий хаммам

СПОРТ И ОТДЫХ:
🏓 Настольный теннис | 🎱 Бильярд | ♟️ Шахматы

УСЛУГИ:
🧺 Стиральная машина | 🔧 Утюг

РАЗНОЕ:
📶 WI-FI""",
        description_uz="""Bizning koteljda yaqinlar bilan dam olish uchun barcha zarur sharoitlar mavjud.

QOIDALAR:
❌ Korparativlar taqiqlangan
❌ Alkogol taqiqlangan
❌ Uy hayvonlari taqiqlangan
❌ RO'G taqiqlangan

⚠️ Agar oilaviy mehmonlar bolasiz kelsa, nikoh guvohnomasini ko'rsatish talab qilinadi.

JADVAL:
• Kirish: 19:00 dan
• Chiqish: 17:00 gacha
• Tinch soatlar: 22:00 dan 07:00 gacha

SIG'IM:
• Mehmonlar: 15 kishi
• Uyqu xonalari: 4 ta
• Karavotlar: 15 ta bir kishilik, 1 ta ikki kishilik

QULAYLIKLAR:
🎮 PlayStation | 🎤 Karaoke | 🖥️ Kompyuter | 🏓 Stol tennisi
🎱 Bilyard | 🏊 Yopiq basseyn 8x4m² qizdiriladi | 🏊 Ochiq basseyn 10x5m²
🍃 Kalyan

HAVODA:
🍖 Yozgi oshxona | 🍢 Barbekyu | 🔥 Mangal

SOG'LIQ:
🧖 Fin saunasi | 🛁 Jakuzi | 🧖 Turk hammomi

SPORT VA DAM OLISH:
🏓 Stol tennisi | 🎱 Bilyard | ♟️ Shaxmat

XIZMATLAR:
🧺 Kir yuvish mashinasi | 🔧 Dazmol

BOSHQA:
📶 WI-FI""",
        description_en="""Our cottage has all the necessary conditions for a relaxing getaway with loved ones.

RULES:
❌ Corporate events prohibited
❌ Alcohol prohibited
❌ Pets prohibited
❌ Registry office ceremonies prohibited

⚠️ If family guests arrive without children, a marriage certificate may be required.

SCHEDULE:
• Check-in: from 19:00
• Check-out: until 17:00
• Quiet hours: from 22:00 to 07:00

CAPACITY:
• Guests: 15 people
• Bedrooms: 4
• Beds: 15 single, 1 double

AMENITIES:
🎮 PlayStation | 🎤 Karaoke | 🖥️ Computer | 🏓 Table tennis
🎱 Billiards | 🏊 Indoor pool 8x4m² heated | 🏊 Outdoor pool 10x5m²
🍃 Hookah

OUTDOOR:
🍖 Summer kitchen | 🍢 Barbecue | 🔥 BBQ

HEALTH & WELLNESS:
🧖 Finnish sauna | 🛁 Jacuzzi | 🧖 Turkish hammam

SPORTS & RECREATION:
🏓 Table tennis | 🎱 Billiards | ♟️ Chess

SERVICES:
🧺 Washing machine | 🔧 Iron

MISCELLANEOUS:
📶 WI-FI""",
        price=Decimal('1500000.00'),
        created_at=timezone.now(),
        
        # Rules (all False = prohibited)
        corporate_allowed=False,
        corporate_rule_ru="❌ Корпоративы запрещены",
        corporate_rule_uz="❌ Korparativlar taqiqlangan",
        corporate_rule_en="❌ Corporate events prohibited",
        
        alcohol_allowed=False,
        alcohol_rule_ru="❌ Алкоголь запрещен",
        alcohol_rule_uz="❌ Alkogol taqiqlangan",
        alcohol_rule_en="❌ Alcohol prohibited",
        
        pets_allowed=False,
        pets_rule_ru="❌ Домашние животные запрещены",
        pets_rule_uz="❌ Uy hayvonlari taqiqlangan",
        pets_rule_en="❌ Pets prohibited",
        
        zags_allowed=False,
        zags_rule_ru="❌ ЗАГС запрещен",
        zags_rule_uz="❌ RO'G taqiqlangan",
        zags_rule_en="❌ Registry office prohibited",
        
        marriage_certificate_required=False,
        marriage_rule_ru="⚠️ Если семейные гости приезжают без детей, потребуется предъявить свидетельство о браке",
        marriage_rule_uz="⚠️ Agar oilaviy mehmonlar bolasiz kelsa, nikoh guvohnomasini ko'rsatish talab qilinadi",
        marriage_rule_en="⚠️ If family guests arrive without children, marriage certificate may be required",
        
        # Schedule
        check_in_time='19:00',
        check_in_rule_ru="С 19:00",
        check_in_rule_uz="19:00 dan",
        check_in_rule_en="From 19:00",
        
        check_out_time='17:00',
        check_out_rule_ru="До 17:00",
        check_out_rule_uz="17:00 gacha",
        check_out_rule_en="Until 17:00",
        
        quiet_hours_start='22:00',
        quiet_hours_end='07:00',
        quiet_hours_rule_ru="С 22:00 до 07:00",
        quiet_hours_rule_uz="22:00 dan 07:00 gacha",
        quiet_hours_rule_en="From 22:00 to 07:00",
        
        # Capacity
        max_guests=15,
        guests_ru="Гости: 15",
        guests_uz="Mehmonlar: 15",
        guests_en="Guests: 15",
        
        bedrooms=4,
        bedrooms_ru="Спальных комнат: 4",
        bedrooms_uz="Uyqu xonalari: 4",
        bedrooms_en="Bedrooms: 4",
        
        beds="15 односпальных, 1 двуспальная",
        beds_ru="Кровати: 15 односпальных, 1 двуспальная",
        beds_uz="Karavotlar: 15 ta bir kishilik, 1 ta ikki kishilik",
        beds_en="Beds: 15 single, 1 double",
        
        # Media & Technologies
        has_playstation=True,
        playstation_ru="🎮 PlayStation",
        playstation_uz="🎮 PlayStation",
        playstation_en="🎮 PlayStation",
        
        has_karaoke=True,
        karaoke_ru="🎤 Караоке",
        karaoke_uz="🎤 Karaoke",
        karaoke_en="🎤 Karaoke",
        
        has_tv=True,
        tv_ru="📺 Телевизор",
        tv_uz="📺 Televizor",
        tv_en="📺 TV",
        
        has_computer=True,
        computer_ru="🖥️ Компьютер",
        computer_uz="🖥️ Kompyuter",
        computer_en="🖥️ Computer",
        
        # Kitchen
        has_kitchen=True,
        kitchen_ru="🍳 Кухня",
        kitchen_uz="🍳 Oshxona",
        kitchen_en="🍳 Kitchen",
        
        has_microwave=True,
        microwave_ru="🔌 Микроволновая печь",
        microwave_uz="🔌 Mikroto'lqin pech",
        microwave_en="🔌 Microwave",
        
        has_refrigerator=True,
        refrigerator_ru="❄️ Холодильник",
        refrigerator_uz="❄️ Muzlatgich",
        refrigerator_en="❄️ Refrigerator",
        
        has_gas_stove=True,
        gas_stove_ru="🔥 Газовая плита",
        gas_stove_uz="🔥 Gaz plita",
        gas_stove_en="🔥 Gas Stove",
        
        # Outdoor
        has_summer_kitchen=True,
        summer_kitchen_ru="🍖 Летняя кухня",
        summer_kitchen_uz="🍖 Yozgi oshxona",
        summer_kitchen_en="🍖 Summer Kitchen",
        
        has_barbecue=True,
        barbecue_ru="🍢 Барбекю",
        barbecue_uz="🍢 Barbekyu",
        barbecue_en="🍢 Barbecue",
        
        has_mangal=True,
        mangal_ru="🔥 Мангал",
        mangal_uz="🔥 Mangal",
        mangal_en="🔥 BBQ",
        
        # Health & Wellness
        has_sauna=True,
        sauna_ru="🧖 Финская сауна",
        sauna_uz="🧖 Fin saunasi",
        sauna_en="🧖 Finnish Sauna",
        sauna_daily_limit_hours=3,
        sauna_rule_ru="Дневной лимит - 3 часа",
        sauna_rule_uz="Kunlik limit - 3 soat",
        sauna_rule_en="Daily limit - 3 hours",
        
        has_salt_room=True,
        salt_room_ru="🧂 Соляная комната",
        salt_room_uz="🧂 Tuz xonasi",
        salt_room_en="🧂 Salt Room",
        
        has_hammam=True,
        hammam_ru="🧖 Турецкий хаммам",
        hammam_uz="🧖 Turk hammomi",
        hammam_en="🧖 Turkish Hammam",
        
        has_jacuzzi=True,
        jacuzzi_ru="🛁 Джакузи",
        jacuzzi_uz="🛁 Jakuzi",
        jacuzzi_en="🛁 Jacuzzi",
        
        # Pools
        has_indoor_pool=True,
        indoor_pool_ru="🏊 Крытый бассейн 8x4м² с подогревом",
        indoor_pool_uz="🏊 Yopiq basseyn 8x4m² qizdiriladi",
        indoor_pool_en="🏊 Indoor pool 8x4m² heated",
        indoor_pool_length=8,
        indoor_pool_width=4,
        indoor_pool_heated=True,
        
        has_outdoor_pool=True,
        outdoor_pool_ru="🏊 Открытый бассейн 10х5м²",
        outdoor_pool_uz="🏊 Ochiq basseyn 10x5m²",
        outdoor_pool_en="🏊 Outdoor pool 10x5m²",
        outdoor_pool_length=10,
        outdoor_pool_width=5,
        
        # Cleaning Services
        has_washing_machine=True,
        washing_machine_ru="🧺 Стиральная машина",
        washing_machine_uz="🧺 Kir yuvish mashinasi",
        washing_machine_en="🧺 Washing Machine",
        
        has_iron=True,
        iron_ru="🔧 Утюг",
        iron_uz="🔧 Dazmol",
        iron_en="🔧 Iron",
        
        # Sports & Recreation
        has_table_tennis=True,
        table_tennis_ru="🏓 Настольный теннис",
        table_tennis_uz="🏓 Stol tennisi",
        table_tennis_en="🏓 Table Tennis",
        
        has_billiards=True,
        billiards_ru="🎱 Бильярд",
        billiards_uz="🎱 Bilyard",
        billiards_en="🎱 Billiards",
        
        has_chess=True,
        chess_ru="♟️ Шахматы",
        chess_uz="♟️ Shaxmat",
        chess_en="♟️ Chess",
        
        has_hookah=True,
        hookah_ru="🍃 Кальян",
        hookah_uz="🍃 Kalyan",
        hookah_en="🍃 Hookah",
        
        # Other
        has_wifi=True,
        wifi_ru="📶 WI-FI",
        wifi_uz="📶 WI-FI",
        wifi_en="📶 WI-FI",
    )
    
    # Create sample blog posts
    Blog.objects.create(
        title_ru="Отдых в загородном коттедже",
        title_uz="Qishloq koteljida dam olish",
        title_en="Country Cottage Vacation",
        description_ru="Отличный отдых вдали от городской суеты. Наш коттедж идеально подходит для семейного отдыха.",
        description_uz="Shahar shovqinidan uzoqda ajoyib dam olish. Bizning kotelj oilaviy dam olish uchun juda mos.",
        description_en="Great vacation away from city noise. Our cottage is perfect for family recreation.",
    )
    
    Blog.objects.create(
        title_ru="Турецкий хаммам и джакузи",
        title_uz="Turk hammomi va jakuzi",
        title_en="Turkish Hammam and Jacuzzi",
        description_ru="Расслабьтесь в нашем турецком хаммаме или насладитесь джакузи после долгого дня.",
        description_uz="Uzun kundan so'ng bizning Turk hammomida yoki jakuzida dam oling.",
        description_en="Relax in our Turkish hammam or enjoy the jacuzzi after a long day.",
    )


def remove_cottage_product(apps, schema_editor):
    Product = apps.get_model('gallery', 'Product')
    Blog = apps.get_model('gallery', 'Blog')
    Product.objects.filter(title_ru="Загородный коттедж «Dacha Go»").delete()
    Blog.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_update_product_fields'),
    ]

    operations = [
        migrations.RunPython(create_cottage_product, remove_cottage_product),
    ]
