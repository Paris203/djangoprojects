from django.contrib import admin
from .models import Menu
from .models import MenuCategory
from .models import Logger
from .models import Reservation
from .models import Customer

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Logger)
admin.site.register(Reservation)
admin.site.register(Customer)




