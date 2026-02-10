from django.core.management.base import BaseCommand
from gallery.models import Product, Blog
from decimal import Decimal


class Command(BaseCommand):
    help = 'Add sample cottage products and blog posts'

    def handle(self, *args, **options):
        # Check if data already exists
        if Product.objects.exists():
            self.stdout.write(self.style.WARNING('Sample data already exists. Skipping.'))
            return

        self.stdout.write('Creating sample cottage products...')
        
        # Cottage 1: Dacha Go Premium
        cottage1 = Product.objects.create(
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

MISCELLANEOUS:
📶 WI-FI""",
            price=Decimal('1500000.00'),
            
            # Rules
            corporate_allowed=False,
            corporate_rule_ru="❌ Корпоративы запрещены",
            alcohol_allowed=False,
            alcohol_rule_ru="❌ Алкоголь запрещен",
            pets_allowed=False,
            pets_rule_ru="❌ Домашние животные запрещены",
            zags_allowed=False,
            zags_rule_ru="❌ ЗАГС запрещен",
            marriage_certificate_required=False,
            marriage_rule_ru="⚠️ Требуется свидетельство о браке",
            
            # Schedule
            check_in_time='19:00',
            check_in_rule_ru="С 19:00",
            check_out_time='17:00',
            check_out_rule_ru="До 17:00",
            quiet_hours_start='22:00',
            quiet_hours_end='07:00',
            quiet_hours_rule_ru="С 22:00 до 07:00",
            
            # Capacity
            max_guests=15,
            guests_ru="Гости: 15",
            bedrooms=4,
            bedrooms_ru="Спальных комнат: 4",
            beds="15 односпальных, 1 двуспальная",
            beds_ru="Кровати: 15 односпальных, 1 двуспальная",
            
            # Media & Technologies
            has_playstation=True,
            playstation_ru="🎮 PlayStation",
            has_karaoke=True,
            karaoke_ru="🎤 Караоке",
            has_tv=True,
            tv_ru="📺 Телевизор",
            has_computer=True,
            computer_ru="🖥️ Компьютер",
            
            # Kitchen
            has_kitchen=True,
            kitchen_ru="🍳 Кухня",
            has_microwave=True,
            has_refrigerator=True,
            has_gas_stove=True,
            
            # Outdoor
            has_summer_kitchen=True,
            summer_kitchen_ru="🍖 Летняя кухня",
            has_barbecue=True,
            barbecue_ru="🍢 Барбекю",
            has_mangal=True,
            mangal_ru="🔥 Мангал",
            
            # Health & Wellness
            has_sauna=True,
            sauna_ru="🧖 Финская сауна",
            sauna_daily_limit_hours=3,
            sauna_rule_ru="Дневной лимит - 3 часа",
            has_salt_room=True,
            salt_room_ru="🧂 Соляная комната",
            has_hammam=True,
            hammam_ru="🧖 Турецкий хаммам",
            has_jacuzzi=True,
            jacuzzi_ru="🛁 Джакузи",
            
            # Pools
            has_indoor_pool=True,
            indoor_pool_ru="🏊 Крытый бассейн 8x4м² с подогревом",
            indoor_pool_length=8,
            indoor_pool_width=4,
            indoor_pool_heated=True,
            has_outdoor_pool=True,
            outdoor_pool_ru="🏊 Открытый бассейн 10х5м²",
            outdoor_pool_length=10,
            outdoor_pool_width=5,
            
            # Cleaning Services
            has_washing_machine=True,
            washing_machine_ru="🧺 Стиральная машина",
            has_iron=True,
            iron_ru="🔧 Утюг",
            
            # Sports & Recreation
            has_table_tennis=True,
            table_tennis_ru="🏓 Настольный теннис",
            has_billiards=True,
            billiards_ru="🎱 Бильярд",
            has_chess=True,
            chess_ru="♟️ Шахматы",
            has_hookah=True,
            hookah_ru="🍃 Кальян",
            
            # Other
            has_wifi=True,
            wifi_ru="📶 WI-FI",
        )
        self.stdout.write(f'Created cottage: {cottage1.title_ru}')

        # Cottage 2: Humsan Hills
        cottage2 = Product.objects.create(
            title_ru="Дача «Humsan Hills»",
            title_uz="«Humsan Hills» dam olish maskani",
            title_en="Cottage «Humsan Hills»",
            description_ru="Прекрасная дача для семейного отдыха вдали от городской суеты.",
            description_uz="Shahar shovqinidan uzoqda oilaviy dam olish uchun ajoyib dam olish maskani.",
            description_en="Beautiful cottage for family vacation away from city noise.",
            price=Decimal('1200000.00'),
            
            # Rules
            corporate_allowed=True,
            corporate_rule_ru="✅ Корпоративы разрешены",
            alcohol_allowed=True,
            alcohol_rule_ru="✅ Алкоголь разрешен",
            pets_allowed=True,
            pets_rule_ru="✅ Домашние животные разрешены",
            zags_allowed=True,
            zags_rule_ru="✅ ЗАГС разрешен",
            marriage_certificate_required=False,
            
            # Schedule
            check_in_time='14:00',
            check_in_rule_ru="С 14:00",
            check_out_time='12:00',
            check_out_rule_ru="До 12:00",
            quiet_hours_start='23:00',
            quiet_hours_end='08:00',
            quiet_hours_rule_ru="С 23:00 до 08:00",
            
            # Capacity
            max_guests=10,
            guests_ru="Гости: 10",
            bedrooms=3,
            bedrooms_ru="Спальных комнат: 3",
            beds="8 односпальных, 1 двуспальная",
            beds_ru="Кровати: 8 односпальных, 1 двуспальная",
            
            # Media & Technologies
            has_playstation=False,
            has_karaoke=True,
            karaoke_ru="🎤 Караоке",
            has_tv=True,
            tv_ru="📺 Телевизор",
            has_computer=False,
            
            # Kitchen
            has_kitchen=True,
            kitchen_ru="🍳 Кухня",
            has_microwave=True,
            has_refrigerator=True,
            has_gas_stove=True,
            
            # Outdoor
            has_summer_kitchen=True,
            summer_kitchen_ru="🍖 Летняя кухня",
            has_barbecue=True,
            barbecue_ru="🍢 Барбекю",
            has_mangal=True,
            mangal_ru="🔥 Мангал",
            
            # Health & Wellness
            has_sauna=False,
            has_salt_room=False,
            has_hammam=True,
            hammam_ru="🧖 Турецкий хаммам",
            has_jacuzzi=True,
            jacuzzi_ru="🛁 Джакузи",
            
            # Pools
            has_indoor_pool=False,
            has_outdoor_pool=True,
            outdoor_pool_ru="🏊 Открытый бассейн",
            outdoor_pool_length=6,
            outdoor_pool_width=4,
            
            # Sports & Recreation
            has_table_tennis=False,
            has_billiards=True,
            billiards_ru="🎱 Бильярд",
            has_chess=True,
            chess_ru="♟️ Шахматы",
            has_hookah=True,
            hookah_ru="🍃 Кальян",
            
            # Other
            has_wifi=True,
            wifi_ru="📶 WI-FI",
        )
        self.stdout.write(f'Created cottage: {cottage2.title_ru}')

        # Cottage 3: Halal Dacha
        cottage3 = Product.objects.create(
            title_ru="Халяль Дача",
            title_uz="Halal Dam Olish Maskani",
            title_en="Halal Cottage",
            description_ru="Отличная дача для семейного отдыха с соблюдением всех халяль традиций.",
            description_uz="Barcha halal an'analariga rioya qilgan holda oilaviy dam olish uchun ajoyib maskan.",
            description_en="Great cottage for family vacation with all halal traditions observed.",
            price=Decimal('1000000.00'),
            
            # Rules - Halal
            corporate_allowed=False,
            corporate_rule_ru="❌ Корпоративы запрещены",
            alcohol_allowed=False,
            alcohol_rule_ru="❌ Алкоголь запрещен",
            pets_allowed=True,
            pets_rule_ru="✅ Домашние животные разрешены",
            zags_allowed=True,
            zags_rule_ru="✅ ЗАГС разрешен",
            marriage_certificate_required=False,
            
            # Schedule
            check_in_time='12:00',
            check_in_rule_ru="С 12:00",
            check_out_time='11:00',
            check_out_rule_ru="До 11:00",
            quiet_hours_start='22:00',
            quiet_hours_end='07:00',
            quiet_hours_rule_ru="С 22:00 до 07:00",
            
            # Capacity
            max_guests=8,
            guests_ru="Гости: 8",
            bedrooms=2,
            bedrooms_ru="Спальных комнат: 2",
            beds="6 односпальных, 1 двуспальная",
            beds_ru="Кровати: 6 односпальных, 1 двуспальная",
            
            # Kitchen
            has_kitchen=True,
            kitchen_ru="🍳 Кухня",
            has_microwave=True,
            has_refrigerator=True,
            has_gas_stove=True,
            
            # Outdoor
            has_summer_kitchen=True,
            summer_kitchen_ru="🍖 Летняя кухня",
            has_barbecue=True,
            barbecue_ru="🍢 Барбекю",
            has_mangal=True,
            mangal_ru="🔥 Мангал",
            
            # Health & Wellness
            has_sauna=False,
            has_hammam=False,
            has_jacuzzi=False,
            
            # Pools
            has_indoor_pool=False,
            has_outdoor_pool=True,
            outdoor_pool_ru="🏊 Открытый бассейн 5x3м²",
            outdoor_pool_length=5,
            outdoor_pool_width=3,
            
            # Sports & Recreation
            has_table_tennis=False,
            has_billiards=False,
            has_chess=True,
            chess_ru="♟️ Шахматы",
            has_hookah=False,
            
            # Other
            has_wifi=True,
            wifi_ru="📶 WI-FI",
        )
        self.stdout.write(f'Created cottage: {cottage3.title_ru}')

        # Cottage 4: Oilalar Uchun
        cottage4 = Product.objects.create(
            title_ru="Оила ва улфатларга",
            title_uz="Oila va Ulfatlar Uchun",
            title_en="Family and Friends",
            description_ru="Идеальное место для семей и друзей. Большой двор, мангал, качели для детей.",
            description_uz="Oila va do'stlar uchun ideal joy. Katta hovli, mangal, bolalar uchun karuselli.",
            description_en="Perfect place for family and friends. Large yard, BBQ, swings for children.",
            price=Decimal('800000.00'),
            
            # Rules
            corporate_allowed=True,
            corporate_rule_ru="✅ Корпоративы разрешены",
            alcohol_allowed=True,
            alcohol_rule_ru="✅ Алкоголь разрешен",
            pets_allowed=True,
            pets_rule_ru="✅ Домашние животные разрешены",
            zags_allowed=True,
            zags_rule_ru="✅ ЗАГС разрешен",
            marriage_certificate_required=False,
            
            # Schedule
            check_in_time='10:00',
            check_in_rule_ru="С 10:00",
            check_out_time='10:00',
            check_out_rule_ru="До 10:00",
            quiet_hours_start='23:00',
            quiet_hours_end='08:00',
            quiet_hours_rule_ru="С 23:00 до 08:00",
            
            # Capacity
            max_guests=12,
            guests_ru="Гости: 12",
            bedrooms=3,
            bedrooms_ru="Спальных комнат: 3",
            beds="10 односпальных",
            beds_ru="Кровати: 10 односпальных",
            
            # Kitchen
            has_kitchen=True,
            kitchen_ru="🍳 Кухня",
            has_microwave=True,
            has_refrigerator=True,
            has_gas_stove=True,
            
            # Outdoor
            has_summer_kitchen=True,
            summer_kitchen_ru="🍖 Летняя кухня",
            has_barbecue=True,
            barbecue_ru="🍢 Барбекю",
            has_mangal=True,
            mangal_ru="🔥 Мангал",
            
            # Pools
            has_indoor_pool=False,
            has_outdoor_pool=True,
            outdoor_pool_ru="🏊 Открытый бассейн",
            outdoor_pool_length=6,
            outdoor_pool_width=3,
            
            # Other
            has_wifi=True,
            wifi_ru="📶 WI-FI",
        )
        self.stdout.write(f'Created cottage: {cottage4.title_ru}')

        # Create sample blog posts
        self.stdout.write('Creating sample blog posts...')
        
        Blog.objects.create(
            title_ru="Отдых в загородном коттедже",
            title_uz="Qishloq koteljida dam olish",
            title_en="Country Cottage Vacation",
            description_ru="Отличный отдых вдали от городской суеты. Наш коттедж идеально подходит для семейного отдыха. Здесь есть всё для комфортного пребывания: бассейн, сауна, караоке и многое другое.",
            description_uz="Shahar shovqinidan uzoqda ajoyib dam olish. Bizning kotelj oilaviy dam olish uchun juda mos. Bu yerda hamma narsa bor: basseyn, sauna, karaoke va boshqalar.",
            description_en="Great vacation away from city noise. Our cottage is perfect for family recreation. Here you have everything for a comfortable stay: pool, sauna, karaoke and more.",
        )
        
        Blog.objects.create(
            title_ru="Турецкий хаммам и джакузи",
            title_uz="Turk hammomi va jakuzi",
            title_en="Turkish Hammam and Jacuzzi",
            description_ru="Расслабьтесь в нашем турецком хаммаме или насладитесь джакузи после долгого дня. Идеальный способ восстановить силы и энергию.",
            description_uz="Uzun kundan so'ng bizning Turk hammomida yoki jakuzida dam oling. Kuch va energiya tiklashning ajoyib usuli.",
            description_en="Relax in our Turkish hammam or enjoy the jacuzzi after a long day. Perfect way to restore strength and energy.",
        )
        
        Blog.objects.create(
            title_ru="Семейный отдых на природе",
            title_uz="Tabiatda oilaviy dam olish",
            title_en="Family Nature Vacation",
            description_ru="Отличная возможность провести время с семьёй на свежем воздухе. Мангал, летняя кухня, качели для детей - всё для идеального семейного отдыха.",
            description_uz="Oila bilan tabiatda vaqt o'tkazishning ajoyib imkoniyati. Mangal, yozgi oshxona, bolalar uchun karuselli - hammasi ideal oilaviy dam olish uchun.",
            description_en="Great opportunity to spend time with family in nature. BBQ, summer kitchen, swings for children - everything for perfect family vacation.",
        )

        self.stdout.write(self.style.SUCCESS('Successfully created sample data!'))
        self.stdout.write(f'Total cottages: {Product.objects.count()}')
        self.stdout.write(f'Total blog posts: {Blog.objects.count()}')
