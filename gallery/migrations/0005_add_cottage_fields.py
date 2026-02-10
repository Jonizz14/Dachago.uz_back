from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_delete_photopost_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='alcohol_allowed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='beds',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='product',
            name='bedrooms',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='product',
            name='check_in_time',
            field=models.CharField(default='19:00', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='check_out_time',
            field=models.CharField(default='17:00', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='corporate_allowed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='has_barbecue',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_billiards',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_hammam',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_hookah',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_jacuzzi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_karaoke',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_mangal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_outdoor_pool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_photo',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='has_playstation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_summer_kitchen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_table_tennis',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_wifi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='marriage_certificate_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='max_guests',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='product',
            name='pets_allowed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pool_length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pool_width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quiet_hours_end',
            field=models.CharField(default='07:00', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='quiet_hours_start',
            field=models.CharField(default='22:00', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='zags_allowed',
            field=models.BooleanField(default=True),
        ),
    ]
