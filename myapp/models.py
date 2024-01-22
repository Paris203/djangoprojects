from django.db import models
from unicodedata import name


# Create your models here.
# class Menu(models.Model):
#     name = models.CharField(max_length=100)
#     cuisine = models.CharField(max_length=100)
#     price = models.IntegerField()
#
#     def __str__(self):
#         return self.name + " : " + self.cuisine


class MenuItems(models.Model):
    items_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    year = models.IntegerField()


class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.menu_category_name


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200)
    reservation_day = models.CharField(max_length=200)
    seats = models.IntegerField()

    def __str__(self):
        return self.name


class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="Enter the exact time")

    def __str__(self):
        return self.first_name + "  " + self.last_name


# class Reservation(models.Model):
#     name = models.CharField(max_length=100, blank=True)
#     contact = models.CharField('Phone number', max_length=300)
#     time = models.TimeField()
#     count = models.IntegerField()
#     notes = models.CharField(max_length=300, blank=True)
#
#     def __str__(self):
#         return self.name
class Reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    booking_time = models.DateTimeField(auto_now=True)
    guest_numberA = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
