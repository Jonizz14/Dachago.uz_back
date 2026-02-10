from django.db import migrations


def add_more_blogs(apps, schema_editor):
    Blog = apps.get_model('gallery', 'Blog')
    
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
    
    Blog.objects.create(
        title_ru="Детская площадка",
        title_uz="Bolalar maydonchasi",
        title_en="Children Playground",
        description_ru="Наши маленькие гости будут в восторге от детской площадки!",
        description_uz="Kichik mehmonlarimiz bolalar maydonchasidan xursand bo'ladilar!",
        description_en="Our little guests will love the children's playground!",
    )
    
    Blog.objects.create(
        title_ru="Финская сауна",
        title_uz="Fin saunasi",
        title_en="Finnish Sauna",
        description_ru="Испытайте настоящую финскую сауну с дневным лимитом 3 часа.",
        description_uz="Haqiqiy fin saunasini sinab ko'ring. Kunlik limit 3 soat.",
        description_en="Try real Finnish sauna with daily limit of 3 hours.",
    )
    
    Blog.objects.create(
        title_ru="Турецкий хаммам",
        title_uz="Turk hammomi",
        title_en="Turkish Hammam",
        description_ru="Наслаждайтесь традиционным турецким хаммамом.",
        description_uz="An'anaviy Turk hammomidan bahramand bo'ling.",
        description_en="Enjoy traditional Turkish hammam.",
    )


def remove_blogs(apps, schema_editor):
    Blog = apps.get_model('gallery', 'Blog')
    Blog.objects.filter(title_ru="Бассейн и сауна").delete()
    Blog.objects.filter(title_ru="Караоке вечер").delete()
    Blog.objects.filter(title_ru="Шашмаком и бильярд").delete()
    Blog.objects.filter(title_ru="Барбекю на природе").delete()
    Blog.objects.filter(title_ru="Детская площадка").delete()
    Blog.objects.filter(title_ru="Финская сауна").delete()
    Blog.objects.filter(title_ru="Турецкий хаммам").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_add_sample_data'),
    ]

    operations = [
        migrations.RunPython(add_more_blogs, remove_blogs),
    ]
