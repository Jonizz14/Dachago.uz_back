from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_remove_product_has_photo_alter_product_photo'),
    ]

    operations = [
        # Rename existing fields to multilingual
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='title_ru',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='description_ru',
        ),
        
        # Add new language fields
        migrations.AddField(
            model_name='product',
            name='title_uz',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        
        # Cottage Rules - add rule text fields
        migrations.AddField(
            model_name='product',
            name='corporate_rule_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Корпоратив"),
        ),
        migrations.AddField(
            model_name='product',
            name='corporate_rule_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Korparativ"),
        ),
        migrations.AddField(
            model_name='product',
            name='corporate_rule_en',
            field=models.TextField(blank=True, null=True, verbose_name="Corporate"),
        ),
        migrations.AddField(
            model_name='product',
            name='alcohol_rule_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Алкоголь"),
        ),
        migrations.AddField(
            model_name='product',
            name='alcohol_rule_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Alkogol"),
        ),
        migrations.AddField(
            model_name='product',
            name='alcohol_rule_en',
            field=models.TextField(blank=True, null=True, verbose_name="Alcohol"),
        ),
        migrations.AddField(
            model_name='product',
            name='pets_rule_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Домашние животные"),
        ),
        migrations.AddField(
            model_name='product',
            name='pets_rule_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Uy hayvonlari"),
        ),
        migrations.AddField(
            model_name='product',
            name='pets_rule_en',
            field=models.TextField(blank=True, null=True, verbose_name="Pets"),
        ),
        migrations.AddField(
            model_name='product',
            name='zags_rule_ru',
            field=models.TextField(blank=True, null=True, verbose_name="ЗАГС"),
        ),
        migrations.AddField(
            model_name='product',
            name='zags_rule_uz',
            field=models.TextField(blank=True, null=True, verbose_name="ROG"),
        ),
        migrations.AddField(
            model_name='product',
            name='zags_rule_en',
            field=models.TextField(blank=True, null=True, verbose_name="Registry Office"),
        ),
        migrations.AddField(
            model_name='product',
            name='marriage_rule_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Свидетельство о браке"),
        ),
        migrations.AddField(
            model_name='product',
            name='marriage_rule_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Nikoh guvohnomasi"),
        ),
        migrations.AddField(
            model_name='product',
            name='marriage_rule_en',
            field=models.TextField(blank=True, null=True, verbose_name="Marriage Certificate"),
        ),
        
        # Schedule - add rule text fields
        migrations.AddField(
            model_name='product',
            name='check_in_rule_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Заезд"),
        ),
        migrations.AddField(
            model_name='product',
            name='check_in_rule_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Kirish"),
        ),
        migrations.AddField(
            model_name='product',
            name='check_in_rule_en',
            field=models.TextField(blank=True, null=True, verbose_name="Check-in"),
        ),
        migrations.AddField(
            model_name='product',
            name='check_out_rule_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Выезд"),
        ),
        migrations.AddField(
            model_name='product',
            name='check_out_rule_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Chiqish"),
        ),
        migrations.AddField(
            model_name='product',
            name='check_out_rule_en',
            field=models.TextField(blank=True, null=True, verbose_name="Check-out"),
        ),
        migrations.AddField(
            model_name='product',
            name='quiet_hours_rule_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Тихие часы"),
        ),
        migrations.AddField(
            model_name='product',
            name='quiet_hours_rule_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Tinch soatlar"),
        ),
        migrations.AddField(
            model_name='product',
            name='quiet_hours_rule_en',
            field=models.TextField(blank=True, null=True, verbose_name="Quiet Hours"),
        ),
        
        # Capacity - add text fields
        migrations.AddField(
            model_name='product',
            name='guests_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Гости"),
        ),
        migrations.AddField(
            model_name='product',
            name='guests_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Mehmonlar"),
        ),
        migrations.AddField(
            model_name='product',
            name='guests_en',
            field=models.TextField(blank=True, null=True, verbose_name="Guests"),
        ),
        migrations.AddField(
            model_name='product',
            name='bedrooms_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Спальных комнат"),
        ),
        migrations.AddField(
            model_name='product',
            name='bedrooms_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Uyqu xonalari"),
        ),
        migrations.AddField(
            model_name='product',
            name='bedrooms_en',
            field=models.TextField(blank=True, null=True, verbose_name="Bedrooms"),
        ),
        migrations.AddField(
            model_name='product',
            name='beds_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Кровати"),
        ),
        migrations.AddField(
            model_name='product',
            name='beds_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Karavotlar"),
        ),
        migrations.AddField(
            model_name='product',
            name='beds_en',
            field=models.TextField(blank=True, null=True, verbose_name="Beds"),
        ),
        
        # Change beds from IntegerField to TextField
        migrations.AlterField(
            model_name='product',
            name='beds',
            field=models.TextField(blank=True, null=True),
        ),
        
        # Media & Technologies
        migrations.AddField(
            model_name='product',
            name='playstation_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Плейстейшн"),
        ),
        migrations.AddField(
            model_name='product',
            name='playstation_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Playstation"),
        ),
        migrations.AddField(
            model_name='product',
            name='playstation_en',
            field=models.TextField(blank=True, null=True, verbose_name="PlayStation"),
        ),
        migrations.AddField(
            model_name='product',
            name='has_tv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='tv_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Телевизор"),
        ),
        migrations.AddField(
            model_name='product',
            name='tv_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Televizor"),
        ),
        migrations.AddField(
            model_name='product',
            name='tv_en',
            field=models.TextField(blank=True, null=True, verbose_name="TV"),
        ),
        migrations.AddField(
            model_name='product',
            name='has_computer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='computer_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Компьютер"),
        ),
        migrations.AddField(
            model_name='product',
            name='computer_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Kompyuter"),
        ),
        migrations.AddField(
            model_name='product',
            name='computer_en',
            field=models.TextField(blank=True, null=True, verbose_name="Computer"),
        ),
        
        # Kitchen
        migrations.AddField(
            model_name='product',
            name='has_kitchen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='kitchen_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Кухня"),
        ),
        migrations.AddField(
            model_name='product',
            name='kitchen_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Oshxona"),
        ),
        migrations.AddField(
            model_name='product',
            name='kitchen_en',
            field=models.TextField(blank=True, null=True, verbose_name="Kitchen"),
        ),
        migrations.AddField(
            model_name='product',
            name='has_microwave',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='microwave_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Микроволновая печь"),
        ),
        migrations.AddField(
            model_name='product',
            name='microwave_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Mikroto'lqin pech"),
        ),
        migrations.AddField(
            model_name='product',
            name='microwave_en',
            field=models.TextField(blank=True, null=True, verbose_name="Microwave"),
        ),
        migrations.AddField(
            model_name='product',
            name='has_refrigerator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='refrigerator_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Холодильник"),
        ),
        migrations.AddField(
            model_name='product',
            name='refrigerator_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Muzlatgich"),
        ),
        migrations.AddField(
            model_name='product',
            name='refrigerator_en',
            field=models.TextField(blank=True, null=True, verbose_name="Refrigerator"),
        ),
        migrations.AddField(
            model_name='product',
            name='has_gas_stove',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='gas_stove_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Газовая плита"),
        ),
        migrations.AddField(
            model_name='product',
            name='gas_stove_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Gaz plita"),
        ),
        migrations.AddField(
            model_name='product',
            name='gas_stove_en',
            field=models.TextField(blank=True, null=True, verbose_name="Gas Stove"),
        ),
        
        # Outdoor
        migrations.AddField(
            model_name='product',
            name='summer_kitchen_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Летняя кухня"),
        ),
        migrations.AddField(
            model_name='product',
            name='summer_kitchen_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Yozgi oshxona"),
        ),
        migrations.AddField(
            model_name='product',
            name='summer_kitchen_en',
            field=models.TextField(blank=True, null=True, verbose_name="Summer Kitchen"),
        ),
        migrations.AddField(
            model_name='product',
            name='barbecue_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Барбекю"),
        ),
        migrations.AddField(
            model_name='product',
            name='barbecue_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Barbekyu"),
        ),
        migrations.AddField(
            model_name='product',
            name='barbecue_en',
            field=models.TextField(blank=True, null=True, verbose_name="Barbecue"),
        ),
        migrations.AddField(
            model_name='product',
            name='mangal_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Мангал"),
        ),
        migrations.AddField(
            model_name='product',
            name='mangal_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Mangal"),
        ),
        migrations.AddField(
            model_name='product',
            name='mangal_en',
            field=models.TextField(blank=True, null=True, verbose_name="BBQ"),
        ),
        
        # Health & Wellness
        migrations.AddField(
            model_name='product',
            name='has_sauna',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sauna_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Финская сауна"),
        ),
        migrations.AddField(
            model_name='product',
            name='sauna_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Fin saunasi"),
        ),
        migrations.AddField(
            model_name='product',
            name='sauna_en',
            field=models.TextField(blank=True, null=True, verbose_name="Finnish Sauna"),
        ),
        migrations.AddField(
            model_name='product',
            name='sauna_daily_limit_hours',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sauna_rule_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Дневной лимит сауны"),
        ),
        migrations.AddField(
            model_name='product',
            name='sauna_rule_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Sauna kunlik limiti"),
        ),
        migrations.AddField(
            model_name='product',
            name='sauna_rule_en',
            field=models.TextField(blank=True, null=True, verbose_name="Sauna daily limit"),
        ),
        migrations.AddField(
            model_name='product',
            name='has_salt_room',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='salt_room_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Соляная комната"),
        ),
        migrations.AddField(
            model_name='product',
            name='salt_room_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Tuz xonasi"),
        ),
        migrations.AddField(
            model_name='product',
            name='salt_room_en',
            field=models.TextField(blank=True, null=True, verbose_name="Salt Room"),
        ),
        migrations.AddField(
            model_name='product',
            name='hammam_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Турецкий хаммам"),
        ),
        migrations.AddField(
            model_name='product',
            name='hammam_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Turk hammomi"),
        ),
        migrations.AddField(
            model_name='product',
            name='hammam_en',
            field=models.TextField(blank=True, null=True, verbose_name="Turkish Hammam"),
        ),
        migrations.AddField(
            model_name='product',
            name='jacuzzi_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Джакузи"),
        ),
        migrations.AddField(
            model_name='product',
            name='jacuzzi_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Jakuzi"),
        ),
        migrations.AddField(
            model_name='product',
            name='jacuzzi_en',
            field=models.TextField(blank=True, null=True, verbose_name="Jacuzzi"),
        ),
        
        # Pools - rename and add new fields
        migrations.RenameField(
            model_name='product',
            old_name='pool_length',
            new_name='outdoor_pool_length',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pool_width',
            new_name='outdoor_pool_width',
        ),
        migrations.AddField(
            model_name='product',
            name='has_indoor_pool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='indoor_pool_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Крытый бассейн"),
        ),
        migrations.AddField(
            model_name='product',
            name='indoor_pool_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Yopiq basseyn"),
        ),
        migrations.AddField(
            model_name='product',
            name='indoor_pool_en',
            field=models.TextField(blank=True, null=True, verbose_name="Indoor Pool"),
        ),
        migrations.AddField(
            model_name='product',
            name='indoor_pool_length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='indoor_pool_width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='indoor_pool_heated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='outdoor_pool_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Открытый бассейн"),
        ),
        migrations.AddField(
            model_name='product',
            name='outdoor_pool_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Ochiq basseyn"),
        ),
        migrations.AddField(
            model_name='product',
            name='outdoor_pool_en',
            field=models.TextField(blank=True, null=True, verbose_name="Outdoor Pool"),
        ),
        
        # Cleaning Services
        migrations.AddField(
            model_name='product',
            name='has_washing_machine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='washing_machine_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Стиральная машина"),
        ),
        migrations.AddField(
            model_name='product',
            name='washing_machine_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Kir yuvish mashinasi"),
        ),
        migrations.AddField(
            model_name='product',
            name='washing_machine_en',
            field=models.TextField(blank=True, null=True, verbose_name="Washing Machine"),
        ),
        migrations.AddField(
            model_name='product',
            name='has_iron',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='iron_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Утюг"),
        ),
        migrations.AddField(
            model_name='product',
            name='iron_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Dazmol"),
        ),
        migrations.AddField(
            model_name='product',
            name='iron_en',
            field=models.TextField(blank=True, null=True, verbose_name="Iron"),
        ),
        
        # Sports & Recreation
        migrations.AddField(
            model_name='product',
            name='table_tennis_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Настольный теннис"),
        ),
        migrations.AddField(
            model_name='product',
            name='table_tennis_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Stol tennisi"),
        ),
        migrations.AddField(
            model_name='product',
            name='table_tennis_en',
            field=models.TextField(blank=True, null=True, verbose_name="Table Tennis"),
        ),
        migrations.AddField(
            model_name='product',
            name='billiards_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Бильярд"),
        ),
        migrations.AddField(
            model_name='product',
            name='billiards_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Bilyard"),
        ),
        migrations.AddField(
            model_name='product',
            name='billiards_en',
            field=models.TextField(blank=True, null=True, verbose_name="Billiards"),
        ),
        migrations.AddField(
            model_name='product',
            name='has_chess',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='chess_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Шахматы"),
        ),
        migrations.AddField(
            model_name='product',
            name='chess_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Shaxmat"),
        ),
        migrations.AddField(
            model_name='product',
            name='chess_en',
            field=models.TextField(blank=True, null=True, verbose_name="Chess"),
        ),
        migrations.AddField(
            model_name='product',
            name='hookah_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Кальян"),
        ),
        migrations.AddField(
            model_name='product',
            name='hookah_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Kalyan"),
        ),
        migrations.AddField(
            model_name='product',
            name='hookah_en',
            field=models.TextField(blank=True, null=True, verbose_name="Hookah"),
        ),
        
        # Other
        migrations.AddField(
            model_name='product',
            name='wifi_ru',
            field=models.TextField(blank=True, null=True, verbose_name="WI-FI"),
        ),
        migrations.AddField(
            model_name='product',
            name='wifi_uz',
            field=models.TextField(blank=True, null=True, verbose_name="WI-FI"),
        ),
        migrations.AddField(
            model_name='product',
            name='wifi_en',
            field=models.TextField(blank=True, null=True, verbose_name="WI-FI"),
        ),
        
        # Blog multilingual fields
        migrations.AddField(
            model_name='blog',
            name='title_uz',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='description_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
    ]
