from django.db import models


class Product(models.Model):
    # Basic Info (multilingual)
    title_ru = models.CharField(max_length=255, blank=True, null=True)
    title_uz = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    
    description_ru = models.TextField(blank=True, null=True)
    description_uz = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    
    photo = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    # Cottage Rules (multilingual)
    # Правила заселения / Qoidalari
    corporate_allowed = models.BooleanField(default=True)
    corporate_rule_ru = models.TextField(blank=True, null=True, verbose_name="Корпоратив")
    corporate_rule_uz = models.TextField(blank=True, null=True, verbose_name="Korparativ")
    corporate_rule_en = models.TextField(blank=True, null=True, verbose_name="Corporate")
    
    alcohol_allowed = models.BooleanField(default=True)
    alcohol_rule_ru = models.TextField(blank=True, null=True, verbose_name="Алкоголь")
    alcohol_rule_uz = models.TextField(blank=True, null=True, verbose_name="Alkogol")
    alcohol_rule_en = models.TextField(blank=True, null=True, verbose_name="Alcohol")
    
    pets_allowed = models.BooleanField(default=True)
    pets_rule_ru = models.TextField(blank=True, null=True, verbose_name="Домашние животные")
    pets_rule_uz = models.TextField(blank=True, null=True, verbose_name="Uy hayvonlari")
    pets_rule_en = models.TextField(blank=True, null=True, verbose_name="Pets")
    
    zags_allowed = models.BooleanField(default=True)
    zags_rule_ru = models.TextField(blank=True, null=True, verbose_name="ЗАГС")
    zags_rule_uz = models.TextField(blank=True, null=True, verbose_name="ROG")
    zags_rule_en = models.TextField(blank=True, null=True, verbose_name="Registry Office")
    
    marriage_certificate_required = models.BooleanField(default=False)
    marriage_rule_ru = models.TextField(blank=True, null=True, verbose_name="Свидетельство о браке")
    marriage_rule_uz = models.TextField(blank=True, null=True, verbose_name="Nikoh guvohnomasi")
    marriage_rule_en = models.TextField(blank=True, null=True, verbose_name="Marriage Certificate")

    # Schedule (multilingual)
    # Расписание / Jadvallar
    check_in_time = models.CharField(max_length=10, default='19:00')
    check_in_rule_ru = models.TextField(blank=True, null=True, verbose_name="Заезд")
    check_in_rule_uz = models.TextField(blank=True, null=True, verbose_name="Kirish")
    check_in_rule_en = models.TextField(blank=True, null=True, verbose_name="Check-in")
    
    check_out_time = models.CharField(max_length=10, default='17:00')
    check_out_rule_ru = models.TextField(blank=True, null=True, verbose_name="Выезд")
    check_out_rule_uz = models.TextField(blank=True, null=True, verbose_name="Chiqish")
    check_out_rule_en = models.TextField(blank=True, null=True, verbose_name="Check-out")
    
    quiet_hours_start = models.CharField(max_length=10, default='22:00')
    quiet_hours_end = models.CharField(max_length=10, default='07:00')
    quiet_hours_rule_ru = models.TextField(blank=True, null=True, verbose_name="Тихие часы")
    quiet_hours_rule_uz = models.TextField(blank=True, null=True, verbose_name="Tinch soatlar")
    quiet_hours_rule_en = models.TextField(blank=True, null=True, verbose_name="Quiet Hours")

    # Capacity (multilingual)
    # Вместимость / Sig'im
    max_guests = models.IntegerField(default=12)
    guests_ru = models.TextField(blank=True, null=True, verbose_name="Гости")
    guests_uz = models.TextField(blank=True, null=True, verbose_name="Mehmonlar")
    guests_en = models.TextField(blank=True, null=True, verbose_name="Guests")
    
    bedrooms = models.IntegerField(default=4)
    bedrooms_ru = models.TextField(blank=True, null=True, verbose_name="Спальных комнат")
    bedrooms_uz = models.TextField(blank=True, null=True, verbose_name="Uyqu xonalari")
    bedrooms_en = models.TextField(blank=True, null=True, verbose_name="Bedrooms")
    
    beds = models.TextField(blank=True, null=True, verbose_name="Кровати")
    beds_ru = models.TextField(blank=True, null=True)
    beds_uz = models.TextField(blank=True, null=True, verbose_name="Karavotlar")
    beds_en = models.TextField(blank=True, null=True, verbose_name="Beds")

    # Media & Technologies (multilingual)
    # Медиа и технологии / Media va texnologiyalar
    has_playstation = models.BooleanField(default=False)
    playstation_ru = models.TextField(blank=True, null=True, verbose_name="Плейстейшн")
    playstation_uz = models.TextField(blank=True, null=True, verbose_name="Playstation")
    playstation_en = models.TextField(blank=True, null=True, verbose_name="PlayStation")
    
    has_karaoke = models.BooleanField(default=False)
    karaoke_ru = models.TextField(blank=True, null=True, verbose_name="Караоке")
    karaoke_uz = models.TextField(blank=True, null=True, verbose_name="Karaoke")
    karaoke_en = models.TextField(blank=True, null=True, verbose_name="Karaoke")
    
    has_tv = models.BooleanField(default=False)
    tv_ru = models.TextField(blank=True, null=True, verbose_name="Телевизор")
    tv_uz = models.TextField(blank=True, null=True, verbose_name="Televizor")
    tv_en = models.TextField(blank=True, null=True, verbose_name="TV")
    
    has_computer = models.BooleanField(default=False)
    computer_ru = models.TextField(blank=True, null=True, verbose_name="Компьютер")
    computer_uz = models.TextField(blank=True, null=True, verbose_name="Kompyuter")
    computer_en = models.TextField(blank=True, null=True, verbose_name="Computer")

    # Kitchen (multilingual)
    # Кухня / Oshxona
    has_kitchen = models.BooleanField(default=False)
    kitchen_ru = models.TextField(blank=True, null=True, verbose_name="Кухня")
    kitchen_uz = models.TextField(blank=True, null=True, verbose_name="Oshxona")
    kitchen_en = models.TextField(blank=True, null=True, verbose_name="Kitchen")
    
    has_microwave = models.BooleanField(default=False)
    microwave_ru = models.TextField(blank=True, null=True, verbose_name="Микроволновая печь")
    microwave_uz = models.TextField(blank=True, null=True, verbose_name="Mikroto'lqin pech")
    microwave_en = models.TextField(blank=True, null=True, verbose_name="Microwave")
    
    has_refrigerator = models.BooleanField(default=False)
    refrigerator_ru = models.TextField(blank=True, null=True, verbose_name="Холодильник")
    refrigerator_uz = models.TextField(blank=True, null=True, verbose_name="Muzlatgich")
    refrigerator_en = models.TextField(blank=True, null=True, verbose_name="Refrigerator")
    
    has_gas_stove = models.BooleanField(default=False)
    gas_stove_ru = models.TextField(blank=True, null=True, verbose_name="Газовая плита")
    gas_stove_uz = models.TextField(blank=True, null=True, verbose_name="Gaz plita")
    gas_stove_en = models.TextField(blank=True, null=True, verbose_name="Gas Stove")

    # Outdoor (multilingual)
    # На свежем воздухе / Havoda
    has_summer_kitchen = models.BooleanField(default=False)
    summer_kitchen_ru = models.TextField(blank=True, null=True, verbose_name="Летняя кухня")
    summer_kitchen_uz = models.TextField(blank=True, null=True, verbose_name="Yozgi oshxona")
    summer_kitchen_en = models.TextField(blank=True, null=True, verbose_name="Summer Kitchen")
    
    has_barbecue = models.BooleanField(default=False)
    barbecue_ru = models.TextField(blank=True, null=True, verbose_name="Барбекю")
    barbecue_uz = models.TextField(blank=True, null=True, verbose_name="Barbekyu")
    barbecue_en = models.TextField(blank=True, null=True, verbose_name="Barbecue")
    
    has_mangal = models.BooleanField(default=False)
    mangal_ru = models.TextField(blank=True, null=True, verbose_name="Мангал")
    mangal_uz = models.TextField(blank=True, null=True, verbose_name="Mangal")
    mangal_en = models.TextField(blank=True, null=True, verbose_name="BBQ")

    # Health & Wellness (multilingual)
    # Оздоровительные / Sog'liq
    has_sauna = models.BooleanField(default=False)
    sauna_ru = models.TextField(blank=True, null=True, verbose_name="Финская сауна")
    sauna_uz = models.TextField(blank=True, null=True, verbose_name="Fin saunasi")
    sauna_en = models.TextField(blank=True, null=True, verbose_name="Finnish Sauna")
    
    sauna_daily_limit_hours = models.IntegerField(blank=True, null=True)
    sauna_rule_ru = models.TextField(blank=True, null=True, verbose_name="Дневной лимит сауны")
    sauna_rule_uz = models.TextField(blank=True, null=True, verbose_name="Sauna kunlik limiti")
    sauna_rule_en = models.TextField(blank=True, null=True, verbose_name="Sauna daily limit")
    
    has_salt_room = models.BooleanField(default=False)
    salt_room_ru = models.TextField(blank=True, null=True, verbose_name="Соляная комната")
    salt_room_uz = models.TextField(blank=True, null=True, verbose_name="Tuz xonasi")
    salt_room_en = models.TextField(blank=True, null=True, verbose_name="Salt Room")
    
    has_hammam = models.BooleanField(default=False)
    hammam_ru = models.TextField(blank=True, null=True, verbose_name="Турецкий хаммам")
    hammam_uz = models.TextField(blank=True, null=True, verbose_name="Turk hammomi")
    hammam_en = models.TextField(blank=True, null=True, verbose_name="Turkish Hammam")
    
    has_jacuzzi = models.BooleanField(default=False)
    jacuzzi_ru = models.TextField(blank=True, null=True, verbose_name="Джакузи")
    jacuzzi_uz = models.TextField(blank=True, null=True, verbose_name="Jakuzi")
    jacuzzi_en = models.TextField(blank=True, null=True, verbose_name="Jacuzzi")

    # Pools
    has_indoor_pool = models.BooleanField(default=False)
    indoor_pool_ru = models.TextField(blank=True, null=True, verbose_name="Крытый бассейн")
    indoor_pool_uz = models.TextField(blank=True, null=True, verbose_name="Yopiq basseyn")
    indoor_pool_en = models.TextField(blank=True, null=True, verbose_name="Indoor Pool")
    
    indoor_pool_length = models.IntegerField(blank=True, null=True)
    indoor_pool_width = models.IntegerField(blank=True, null=True)
    indoor_pool_heated = models.BooleanField(default=False)
    
    has_outdoor_pool = models.BooleanField(default=False)
    outdoor_pool_ru = models.TextField(blank=True, null=True, verbose_name="Открытый бассейн")
    outdoor_pool_uz = models.TextField(blank=True, null=True, verbose_name="Ochiq basseyn")
    outdoor_pool_en = models.TextField(blank=True, null=True, verbose_name="Outdoor Pool")
    
    outdoor_pool_length = models.IntegerField(blank=True, null=True)
    outdoor_pool_width = models.IntegerField(blank=True, null=True)

    # Cleaning Services (multilingual)
    # Услуги уборки / Tozalash xizmatlari
    has_washing_machine = models.BooleanField(default=False)
    washing_machine_ru = models.TextField(blank=True, null=True, verbose_name="Стиральная машина")
    washing_machine_uz = models.TextField(blank=True, null=True, verbose_name="Kir yuvish mashinasi")
    washing_machine_en = models.TextField(blank=True, null=True, verbose_name="Washing Machine")
    
    has_iron = models.BooleanField(default=False)
    iron_ru = models.TextField(blank=True, null=True, verbose_name="Утюг")
    iron_uz = models.TextField(blank=True, null=True, verbose_name="Dazmol")
    iron_en = models.TextField(blank=True, null=True, verbose_name="Iron")

    # Sports & Recreation (multilingual)
    # Спорт и отдых / Sport va dam olish
    has_table_tennis = models.BooleanField(default=False)
    table_tennis_ru = models.TextField(blank=True, null=True, verbose_name="Настольный теннис")
    table_tennis_uz = models.TextField(blank=True, null=True, verbose_name="Stol tennisi")
    table_tennis_en = models.TextField(blank=True, null=True, verbose_name="Table Tennis")
    
    has_billiards = models.BooleanField(default=False)
    billiards_ru = models.TextField(blank=True, null=True, verbose_name="Бильярд")
    billiards_uz = models.TextField(blank=True, null=True, verbose_name="Bilyard")
    billiards_en = models.TextField(blank=True, null=True, verbose_name="Billiards")
    
    has_chess = models.BooleanField(default=False)
    chess_ru = models.TextField(blank=True, null=True, verbose_name="Шахматы")
    chess_uz = models.TextField(blank=True, null=True, verbose_name="Shaxmat")
    chess_en = models.TextField(blank=True, null=True, verbose_name="Chess")
    
    has_hookah = models.BooleanField(default=False)
    hookah_ru = models.TextField(blank=True, null=True, verbose_name="Кальян")
    hookah_uz = models.TextField(blank=True, null=True, verbose_name="Kalyan")
    hookah_en = models.TextField(blank=True, null=True, verbose_name="Hookah")

    # Other (multilingual)
    # Разное / Boshqa
    has_wifi = models.BooleanField(default=False)
    wifi_ru = models.TextField(blank=True, null=True, verbose_name="WI-FI")
    wifi_uz = models.TextField(blank=True, null=True, verbose_name="WI-FI")
    wifi_en = models.TextField(blank=True, null=True, verbose_name="WI-FI")

    def __str__(self):
        return self.title_ru or self.title_uz or self.title_en or "Product"
    
    @property
    def title(self):
        """Get title in available language (priority: Russian, Uzbek, English)"""
        return self.title_ru or self.title_uz or self.title_en
    
    @property
    def description(self):
        """Get description in available language (priority: Russian, Uzbek, English)"""
        return self.description_ru or self.description_uz or self.description_en


class Blog(models.Model):
    title_ru = models.CharField(max_length=255)
    title_uz = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    
    description_ru = models.TextField()
    description_uz = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    
    photo = models.ImageField(upload_to='blogs/')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_ru
