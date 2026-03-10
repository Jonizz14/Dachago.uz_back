import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from gallery.models import Product, Blog

class Command(BaseCommand):
    help = 'Add 100 diverse sample cottage products'

    def handle(self, *args, **options):
        # Clear existing products to avoid duplicates
        Product.objects.all().delete()
        self.stdout.write('Deleted existing products.')

        prefixes_ru = ["Элитная", "Уютная", "Семейная", "Премиум", "Горная", "Лесная", "Зимняя", "Летняя", "Современная", "Традиционная"]
        prefixes_uz = ["Hashamatli", "Shinam", "Oilaviy", "Premium", "Tog'dagi", "O'rmondagi", "Qishki", "Yozgi", "Zamonaviy", "Milliy"]
        
        types_ru = ["Дача", "Вилла", "Коттедж", "Усадьба", "Резиденция"]
        types_uz = ["Dacha", "Villa", "Kottej", "Xonadon", "Qasrxona"]
        
        locations_ru = ["Чорвок", "Хумсан", "Бочка", "Юсупхона", "Бричмулла", "Нанай", "Бурчмулла", "Янгиабад", "Пскент", "Сукок"]
        locations_uz = ["Chorvoq", "Humsan", "Bochka", "Yusuphona", "Brichmulla", "Nanay", "Burchmulla", "Yangiabod", "Piskent", "Suqoq"]

        self.stdout.write('Generating 100 cottages...')
        
        for i in range(1, 101):
            p_idx = random.randint(0, len(prefixes_ru)-1)
            t_idx = random.randint(0, len(types_ru)-1)
            l_idx = random.randint(0, len(locations_ru)-1)
            
            title_ru = f"{prefixes_ru[p_idx]} {types_ru[t_idx]} в {locations_ru[l_idx]} №{i}"
            title_uz = f"{locations_uz[l_idx]}dagi {prefixes_uz[p_idx]} {types_uz[t_idx]} №{i}"
            title_en = f"{prefixes_ru[p_idx]} {types_ru[t_idx]} in {locations_ru[l_idx]} #{i}"
            
            price = Decimal(random.randint(500, 5000)) * 1000  # 500k to 5M
            
            # Random boolean features
            has_sauna = random.choice([True, False])
            has_pool = random.choice([True, False])
            has_wifi = random.choice([True, True, False]) # More likely to have wifi
            has_ps = random.choice([True, False, False])
            has_karaoke = random.choice([True, False])
            has_tapchan = random.choice([True, True, False])
            has_fireplace = random.choice([True, False])
            
            cottage = Product.objects.create(
                title_ru=title_ru,
                title_uz=title_uz,
                title_en=title_en,
                description_ru=f"Прекрасное место для отдыха {i}. Расположено в живописном районе {locations_ru[l_idx]}.",
                description_uz=f"{locations_uz[l_idx]} hududidagi ajoyib dam olish maskani {i}.",
                description_en=f"A wonderful place for relaxation #{i} in {locations_ru[l_idx]}.",
                price=price,
                
                # Capacity (ONLY NUMBERS)
                max_guests=random.randint(4, 30),
                bedrooms=random.randint(2, 8),
                bathrooms=random.randint(1, 4),
                floors=random.randint(1, 3),
                total_area=random.randint(100, 600),
                land_area=Decimal(random.randint(2, 20)),
                parking_places=random.randint(1, 6),
                
                # Rules
                corporate_allowed=random.choice([True, False]),
                alcohol_allowed=random.choice([True, False]),
                pets_allowed=random.choice([True, False]),
                zags_allowed=random.choice([True, False]),
                
                # Features
                has_sauna=has_sauna,
                has_indoor_pool=has_pool and random.choice([True, False]),
                has_outdoor_pool=has_pool or random.choice([True, False]),
                has_wifi=has_wifi,
                has_playstation=has_ps,
                has_karaoke=has_karaoke,
                has_tapchan=has_tapchan,
                has_fireplace=has_fireplace,
                has_kitchen=True,
                has_refrigerator=True,
                has_gas_stove=True,
                has_billiards=random.choice([True, False, False]),
                has_table_tennis=random.choice([True, False, False]),
                
                # Times
                check_in_time="14:00",
                check_out_time="12:00",
            )
            
        self.stdout.write(self.style.SUCCESS(f'Successfully created 100 unique cottages!'))
