from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000,default="")
    image_url = models.ImageField(upload_to="media/img/menu_items",blank=True,null=True)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class Reservation(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    reservation_count = models.PositiveIntegerField()
    reservation_date = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name