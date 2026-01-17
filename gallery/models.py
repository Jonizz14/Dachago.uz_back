from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='blogs/')
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True) # qo'yilgan sana

    def __str__(self):
        return self.title
