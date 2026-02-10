from django.db import migrations
from django.utils import timezone
from decimal import Decimal


def create_cottage_product(apps, schema_editor):
    # Use direct database access to avoid historical model issues
    from django.db import connection
    cursor = connection.cursor()
    
    # Insert the cottage product directly
    cursor.execute("""
        INSERT INTO gallery_product (
            title_ru, title_uz, title_en,
            description_ru, description_uz, description_en,
            photo, price, created_at,
            corporate_allowed, corporate_rule_ru, corporate_rule_uz, corporate_rule_en,
            alcohol_allowed, alcohol_rule_ru, alcohol_rule_uz, alcohol_rule_en,
            pets_allowed, pets_rule_ru, pets_rule_uz, pets_rule_en,
            zags_allowed, zags_rule_ru, zags_rule_uz, zags_rule_en,
            marriage_certificate_required, marriage_rule_ru, marriage_rule_uz, marriage_rule_en,
            check_in_time, check_in_rule_ru, check_in_rule_uz, check_in_rule_en,
            check_out_time, check_out_rule_ru, check_out_rule_uz, check_out_rule_en,
            quiet_hours_start, quiet_hours_end, quiet_hours_rule_ru, quiet_hours_rule_uz, quiet_hours_rule_en,
            max_guests, guests_ru, guests_uz, guests_en,
            bedrooms, bedrooms_ru, bedrooms_uz, bedrooms_en,
            beds, beds_ru, beds_uz, beds_en,
            has_playstation, playstation_ru, playstation_uz, playstation_en,
            has_karaoke, karaoke_ru, karaoke_uz, karaoke_en,
            has_tv, tv_ru, tv_uz, tv_en,
            has_computer, computer_ru, computer_uz, computer_en,
            has_kitchen, kitchen_ru, kitchen_uz, kitchen_en,
            has_microwave, microwave_ru, microwave_uz, microwave_en,
            has_refrigerator, refrigerator_ru, refrigerator_uz, refrigerator_en,
            has_gas_stove, gas_stove_ru, gas_stove_uz, gas_stove_en,
            has_summer_kitchen, summer_kitchen_ru, summer_kitchen_uz, summer_kitchen_en,
            has_barbecue, barbecue_ru, barbecue_uz, barbecue_en,
            has_mangal, mangal_ru, mangal_uz, mangal_en,
            has_sauna, sauna_ru, sauna_uz, sauna_en,
            sauna_daily_limit_hours, sauna_rule_ru, sauna_rule_uz, sauna_rule_en,
            has_salt_room, salt_room_ru, salt_room_uz, salt_room_en,
            has_hammam, hammam_ru, hammam_uz, hammam_en,
            has_jacuzzi, jacuzzi_ru, jacuzzi_uz, jacuzzi_en,
            has_indoor_pool, indoor_pool_ru, indoor_pool_uz, indoor_pool_en,
            indoor_pool_length, indoor_pool_width, indoor_pool_heated,
            has_outdoor_pool, outdoor_pool_ru, outdoor_pool_uz, outdoor_pool_en,
            outdoor_pool_length, outdoor_pool_width,
            has_washing_machine, washing_machine_ru, washing_machine_uz, washing_machine_en,
            has_iron, iron_ru, iron_uz, iron_en,
            has_table_tennis, table_tennis_ru, table_tennis_uz, table_tennis_en,
            has_billiards, billiards_ru, billiards_uz, billiards_en,
            has_chess, chess_ru, chess_uz, chess_en,
            has_hookah, hookah_ru, hookah_uz, hookah_en,
            has_wifi, wifi_ru, wifi_uz, wifi_en
        ) VALUES (
            %s, %s, %s, %s, %s, %s, NULL, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
    """, [
        # Basic Info
        "Загородный коттедж «Dacha Go»",
        "«Dacha Go» qishloq kotlaji",
        "Country Cottage «Dacha Go»",
        """В нашем коттедже есть все необходимые условия для отдыха с близкими.

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
        """Bizning koteljda yaqinlar bilan dam olish uchun barcha zarur sharoitlar mavjud.

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
        """Our cottage has all the necessary conditions for a relaxing getaway with loved ones.

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
        '1500000.00',
        timezone.now(),
        
        # Rules (all False = prohibited)
        False, "❌ Корпоративы запрещены", "❌ Korparativlar taqiqlangan", "❌ Corporate events prohibited",
        False, "❌ Алкоголь запрещен", "❌ Alkogol taqiqlangan", "❌ Alcohol prohibited",
        False, "❌ Домашние животные запрещены", "❌ Uy hayvonlari taqiqlangan", "❌ Pets prohibited",
        False, "❌ ЗАГС запрещен", "❌ RO'G taqiqlangan", "❌ Registry office prohibited",
        False, "⚠️ Если семейные гости приезжают без детей, потребуется предъявить свидетельство о браке", "⚠️ Agar oilaviy mehmonlar bolasiz kelsa, nikoh guvohnomasini ko'rsatish talab qilinadi", "⚠️ If family guests arrive without children, marriage certificate may be required",
        
        # Schedule
        '19:00', "С 19:00", "19:00 dan", "From 19:00",
        '17:00', "До 17:00", "17:00 gacha", "Until 17:00",
        '22:00', '07:00', "С 22:00 до 07:00", "22:00 dan 07:00 gacha", "From 22:00 to 07:00",
        
        # Capacity
        15, "Гости: 15", "Mehmonlar: 15", "Guests: 15",
        4, "Спальных комнат: 4", "Uyqu xonalari: 4", "Bedrooms: 4",
        "15 односпальных, 1 двуспальная", "Кровати: 15 односпальных, 1 двуспальная", "Karavotlar: 15 ta bir kishilik, 1 ta ikki kishilik", "Beds: 15 single, 1 double",
        
        # Media & Technologies
        True, "🎮 PlayStation", "🎮 PlayStation", "🎮 PlayStation",
        True, "🎤 Караоке", "🎤 Karaoke", "🎤 Karaoke",
        True, "📺 Телевизор", "📺 Televizor", "📺 TV",
        True, "🖥️ Компьютер", "🖥️ Kompyuter", "🖥️ Computer",
        
        # Kitchen
        True, "🍳 Кухня", "🍳 Oshxona", "🍳 Kitchen",
        True, "🔌 Микроволновая печь", "🔌 Mikroto'lqin pech", "🔌 Microwave",
        True, "❄️ Холодильник", "❄️ Muzlatgich", "❄️ Refrigerator",
        True, "🔥 Газовая плита", "🔥 Gaz plita", "🔥 Gas Stove",
        
        # Outdoor
        True, "🍖 Летняя кухня", "🍖 Yozgi oshxona", "🍖 Summer Kitchen",
        True, "🍢 Барбекю", "🍢 Barbekyu", "🍢 Barbecue",
        True, "🔥 Мангал", "🔥 Mangal", "🔥 BBQ",
        
        # Health & Wellness
        True, "🧖 Финская сауна", "🧖 Fin saunasi", "🧖 Finnish Sauna",
        3, "Дневной лимит - 3 часа", "Kunlik limit - 3 soat", "Daily limit - 3 hours",
        True, "🧂 Соляная комната", "🧂 Tuz xonasi", "🧂 Salt Room",
        True, "🧖 Турецкий хаммам", "🧖 Turk hammomi", "🧖 Turkish Hammam",
        True, "🛁 Джакузи", "🛁 Jakuzi", "🛁 Jacuzzi",
        
        # Pools
        True, "🏊 Крытый бассейн 8x4м² с подогревом", "🏊 Yopiq basseyn 8x4m² qizdiriladi", "🏊 Indoor pool 8x4m² heated",
        8, 4, True,
        True, "🏊 Открытый бассейн 10х5м²", "🏊 Ochiq basseyn 10x5m²", "🏊 Outdoor pool 10x5m²",
        10, 5,
        
        # Cleaning Services
        True, "🧺 Стиральная машина", "🧺 Kir yuvish mashinasi", "🧺 Washing Machine",
        True, "🔧 Утюг", "🔧 Dazmol", "🔧 Iron",
        
        # Sports & Recreation
        True, "🏓 Настольный теннис", "🏓 Stol tennisi", "🏓 Table Tennis",
        True, "🎱 Бильярд", "🎱 Bilyard", "🎱 Billiards",
        True, "♟️ Шахматы", "♟️ Shaxmat", "♟️ Chess",
        True, "🍃 Кальян", "🍃 Kalyan", "🍃 Hookah",
        
        # Other
        True, "📶 WI-FI", "📶 WI-FI", "📶 WI-FI",
    ])
    
    # Insert sample blog posts
    cursor.execute("""
        INSERT INTO gallery_blog (title_ru, title_uz, title_en, description_ru, description_uz, description_en, photo, published_date)
        VALUES (%s, %s, %s, %s, %s, %s, NULL, %s)
    """, [
        "Отдых в загородном коттедже",
        "Qishloq koteljida dam olish",
        "Country Cottage Vacation",
        "Отличный отдых вдали от городской суеты. Наш коттедж идеально подходит для семейного отдыха.",
        "Shahar shovqinidan uzoqda ajoyib dam olish. Bizning kotelj oilaviy dam olish uchun juda mos.",
        "Great vacation away from city noise. Our cottage is perfect for family recreation.",
        timezone.now()
    ])
    
    cursor.execute("""
        INSERT INTO gallery_blog (title_ru, title_uz, title_en, description_ru, description_uz, description_en, photo, published_date)
        VALUES (%s, %s, %s, %s, %s, %s, NULL, %s)
    """, [
        "Турецкий хаммам и джакузи",
        "Turk hammomi va jakuzi",
        "Turkish Hammam and Jacuzzi",
        "Расслабьтесь в нашем турецком хаммаме или насладитесь джакузи после долгого дня.",
        "Uzun kundan so'ng bizning Turk hammomida yoki jakuzida dam oling.",
        "Relax in our Turkish hammam or enjoy the jacuzzi after a long day.",
        timezone.now()
    ])


def remove_cottage_product(apps, schema_editor):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("DELETE FROM gallery_product WHERE title_ru = %s", ["Загородный коттедж «Dacha Go»"])
    cursor.execute("DELETE FROM gallery_blog")


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_update_product_fields'),
    ]

    operations = [
        migrations.RunPython(create_cottage_product, remove_cottage_product),
    ]
