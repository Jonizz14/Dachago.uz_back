from django.core.management.base import BaseCommand
from gallery.models import Product, Blog, CottageAvailability, Booking, Review, Activity, Employee, Payment, Service, Announcement, Settings
from django.contrib.auth.models import User
import random
from datetime import date, timedelta, datetime
from django.utils import timezone
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seeds the database with mock data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        # 1. Create a superuser if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write('Superuser created: admin/admin123')

        # 3. Create Products (Dachas)
        categories = ['Mountain', 'Villa', 'Lake', 'Cottage', 'Beach']
        cities = ['Bochiston', 'Chimyon', 'Amirsoy', 'Charvoq', 'Xumsan', 'Oqtosh']
        
        products = []
        for i in range(1, 11):
            category = random.choice(categories)
            city = random.choice(cities)
            price = random.randint(500, 5000) * 1000
            
            p = Product.objects.create(
                title_ru=f"Роскошная дача {i} в {city}",
                title_uz=f"Hashamatli dacha {i} - {city}da",
                title_en=f"Luxury Dacha {i} in {city}",
                description_ru=f"Прекрасная дача в горах с бассейном и всеми удобствами. Идеально для отдыха с семьей. Номер {i}.",
                description_uz=f"Tog' bag'ridagi barcha sharoitlarga ega go'zal dacha. Oila bilan dam olish uchun ideal. Raqam {i}.",
                description_en=f"Beautiful cottage in the mountains with pool and all amenities. Ideal for family holidays. Number {i}.",
                price=Decimal(price),
                category=category,
                status='active',
                latitude=str(41.6 + random.random() * 0.1),
                longitude=str(69.9 + random.random() * 0.1),
                location_name=city,
                max_guests=random.randint(6, 20),
                bedrooms=random.randint(2, 6),
                bathrooms=random.randint(1, 3),
                floors=random.randint(1, 3),
                total_area=random.randint(150, 500),
                land_area=Decimal(random.randint(4, 20)),
                parking_places=random.randint(2, 6),
                has_tapchan=random.choice([True, False]),
                has_fireplace=random.choice([True, False]),
                has_playstation=random.choice([True, False]),
                has_karaoke=random.choice([True, False]),
                has_tv=True,
                has_kitchen=True,
                has_microwave=True,
                has_refrigerator=True,
                has_gas_stove=True,
                has_summer_kitchen=random.choice([True, False]),
                has_barbecue=True,
                has_mangal=True,
                has_sauna=random.choice([True, False]),
                has_indoor_pool=random.choice([True, False]),
                has_outdoor_pool=True,
                has_wifi=True
            )
            products.append(p)
            
        self.stdout.write(f'Created {len(products)} products.')

        # 4. Create Availability
        today = date.today()
        for p in products:
            for i in range(15):
                d = today + timedelta(days=i)
                if random.random() > 0.7:  # 30% chance to be busy
                    CottageAvailability.objects.get_or_create(product=p, date=d, is_busy=True)
        
        self.stdout.write('Cottage availability seeded.')

        # 5. Create Blogs
        for i in range(1, 6):
            Blog.objects.create(
                title_ru=f"Советы для отдыха в горах #{i}",
                title_uz=f"Tog'da dam olish bo'yicha maslahatlar #{i}",
                title_en=f"Tips for mountain vacation #{i}",
                description_ru="Текст блога c полезными советами для туристов и отдыхающих.",
                description_uz="Turistlar va dam oluvchilar uchun foydali maslahatlar bilan blog matni.",
                description_en="Blog text with useful tips for tourists and vacationers."
            )
        
        self.stdout.write('Blogs seeded.')

        # 6. Create Reviews
        names = ['Ali', 'Vali', 'Guli', 'Jonibek', 'Sevara', 'Anvar']
        for p in products:
            for _ in range(random.randint(1, 3)):
                Review.objects.create(
                    product=p,
                    user_name=random.choice(names),
                    rating=random.randint(4, 5),
                    comment=random.choice(["Zo'r joy ekan!", "Mazxa qildik.", "Everything was perfect.", "Juda yoqdi.", "Отличное место!"]),
                    status='approved'
                )
        
        self.stdout.write('Reviews seeded.')

        # 7. Create Employees
        positions = ['Manager', 'Cleaner', 'Security', 'Owner', 'Support']
        for i in range(1, 7):
            Employee.objects.create(
                name=f"Xodim {i}",
                position=random.choice(positions),
                email=f"employee{i}@example.com",
                phone=f"+998 90 000 00 0{i}",
                status='active'
            )
            
        self.stdout.write('Employees seeded.')

        # 8. Create Payments
        for i in range(1, 21):
            Payment.objects.create(
                transaction_id=f"PAY-{1000+i}",
                customer_name=random.choice(names),
                cottage_name=f"Dacha {random.randint(1, 10)}",
                amount=Decimal(random.randint(100, 1000) * 1000),
                method=random.choice(['PayMe', 'Click', 'Cash', 'Card']),
                status=random.choice(['completed', 'pending', 'completed']),
                date=today - timedelta(days=random.randint(1, 30))
            )
            
        self.stdout.write('Payments seeded.')

        # 9. Create Services
        services = [
            ("Oshpaz xizmati", 200000, "Kuniga"),
            ("Tozalash xizmati", 150000, "Marta"),
            ("Transfe", 100000, "Marta"),
            ("O'tin", 50000, "Bog'lam"),
        ]
        for name, price, duration in services:
            Service.objects.get_or_create(
                name=name,
                price=Decimal(price),
                duration=duration,
                status='active'
            )
            
        self.stdout.write('Services seeded.')

        # 10. Create Announcements
        for i in range(1, 6):
            Announcement.objects.create(
                title=f"Yangilik #{i}",
                content="Tez orada yangi dacha qo'shiladi. Bizni kuzatib boring!",
                date=today + timedelta(days=random.randint(1, 10)),
                status='active',
                views=random.randint(10, 500)
            )
            
        self.stdout.write('Announcements seeded.')

        # 11. Create Activities
        activity_titles = ["Yangi bron", "Yangi mijoz", "To'lov qabul qilindi", "Sharh qoldirildi"]
        for i in range(1, 11):
            Activity.objects.create(
                title=random.choice(activity_titles),
                description=f"Foydalanuvchi tomonidan amalga oshirildi {i}",
                icon_type=random.choice(['user', 'shopping', 'dollar', 'message'])
            )
            
        self.stdout.write('Activities seeded.')

        # 12. Settings
        if not Settings.objects.exists():
            Settings.objects.create(
                site_name='DachaGo',
                contact_email='contact@dachago.uz',
                contact_phone='+998 71 200 01 02'
            )
            self.stdout.write('Settings initialized.')

        self.stdout.write(self.style.SUCCESS('Successfully seeded all data!'))
