from django.core.management.base import BaseCommand
from gallery.models import Product, Blog
from decimal import Decimal


class Command(BaseCommand):
    help = 'Add sample cottage products and blog posts'

    def handle(self, *args, **options):
        # Clear existing data
        Product.objects.all().delete()
        Blog.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Cleared existing data.'))

        self.stdout.write('Creating 25 detailed multilingual cottage products...')
        import random
        
        # Data lists for variety
        locations = [
            {"ru": "Чорвок", "uz": "Chorvoq", "en": "Chorvok"},
            {"ru": "Хумсан", "uz": "Humsan", "en": "Humsan"},
            {"ru": "Бочка", "uz": "Bochka", "en": "Bochka"},
            {"ru": "Юсупхона", "uz": "Yusuphona", "en": "Yusuphona"},
            {"ru": "Бричмулла", "uz": "Brichmulla", "en": "Brichmulla"},
            {"ru": "Акча", "uz": "Akcha", "en": "Akcha"},
            {"ru": "Янгиабад", "uz": "Yangiabod", "en": "Yangiabad"},
            {"ru": "Сиджак", "uz": "Sijjak", "en": "Sijak"},
        ]
        
        styles = [
            {"ru": "Премиум Коттедж", "uz": "Premium Kottej", "en": "Premium Cottage"},
            {"ru": "Семейная Дача", "uz": "Oilaviy Dacha", "en": "Family Dacha"},
            {"ru": "Современная Вилла", "uz": "Zamonaviy Villa", "en": "Modern Villa"},
            {"ru": "Уютный Домик", "uz": "Shinam Uy", "en": "Cozy House"},
            {"ru": "Горная Резиденция", "uz": "Tog' Bag'ridagi Qasrxona", "en": "Mountain Residence"},
        ]

        descriptions = [
            {
                "ru": "Прекрасное место для отдыха с семьей и друзьями. Чистый воздух, отличный вид и все удобства.",
                "uz": "Oila va do'stlar bilan dam olish uchun ajoyib joy. Toza havo, go'zal manzara va barcha qulayliklar.",
                "en": "A wonderful place to relax with family and friends. Fresh air, great views and all amenities."
            },
            {
                "ru": "Элитный отдых в живописном районе. Бассейн с подогревом, сауна и современная кухня.",
                "uz": "Go'zal hududda elita dam olish maskani. Isitiladigan basseyn, sauna va zamonaviy oshxona.",
                "en": "Elite relaxation in a picturesque area. Heated pool, sauna and modern kitchen."
            },
            {
                "ru": "Тихое и спокойное место для тех, кто хочет отдохнуть от городской суеты.",
                "uz": "Shahar shovqinidan dam olmoqchi bo'lganlar uchun sokin va tinch joy.",
                "en": "A quiet and peaceful place for those who want to take a break from the city bustle."
            }
        ]

        for i in range(1, 26):
            loc = random.choice(locations)
            style = random.choice(styles)
            desc = random.choice(descriptions)
            
            title_ru = f"{style['ru']} «{loc['ru']} View» №{i}"
            title_uz = f"«{loc['uz']} View» {style['uz']} №{i}"
            title_en = f"{style['en']} «{loc['en']} View» #{i}"
            
            # Numeric fields
            max_guests = random.randint(6, 25)
            bedrooms = random.randint(2, 7)
            bathrooms = random.randint(1, 3)
            floors = random.randint(1, 3)
            total_area = random.randint(150, 500)
            land_area = Decimal(random.randint(4, 15))
            parking_places = random.randint(2, 5)
            
            price = Decimal(random.randint(800, 4500)) * 1000

            Product.objects.create(
                title_ru=title_ru,
                title_uz=title_uz,
                title_en=title_en,
                description_ru=desc['ru'],
                description_uz=desc['uz'],
                description_en=desc['en'],
                price=price,
                
                # Capacity (NUMBERS ONLY)
                max_guests=max_guests,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                floors=floors,
                total_area=total_area,
                land_area=land_area,
                parking_places=parking_places,
                
                # Rules
                corporate_allowed=random.choice([True, False]),
                alcohol_allowed=random.choice([True, False]),
                pets_allowed=random.choice([True, False]),
                zags_allowed=random.choice([True, False]),
                marriage_certificate_required=random.choice([True, False]),
                
                # Amenities
                has_sauna=random.choice([True, False]),
                has_indoor_pool=random.choice([True, False]),
                has_outdoor_pool=True,
                has_wifi=True,
                has_tapchan=random.choice([True, True, False]),
                has_fireplace=random.choice([True, False]),
                has_karaoke=random.choice([True, False]),
                has_playstation=random.choice([True, False]),
                has_kitchen=True,
                has_refrigerator=True,
                has_gas_stove=True,
                
                # Times
                check_in_time="14:00",
                check_out_time="12:00",
            )

        self.stdout.write('Creating sample blog posts...')
        Blog.objects.create(
            title_ru="Лучшие места для отдыха 2026",
            title_uz="2026-yilning eng yaxshi dam olish maskanlari",
            title_en="Best Vacation Spots 2026",
            description_ru="Обзор самых популярных коттеджей в этом сезоне.",
            description_uz="Ushbu mavsumdagi eng ommabop kottejlar sharhi.",
            description_en="Overview of the most popular cottages this season.",
        )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created 25 high-quality multilingual products!'))
