from django.contrib import admin
from home.models import Contact

from .models import  User_profile
from .models import UserProfile

from .models import MenuItem

admin.site.register(MenuItem)
from django.contrib import admin
from .models import Chef

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'designation')

# Register your models here.


admin.site.register(UserProfile)

admin.site.register(User_profile)
admin.site.register(Contact)


# from django.contrib import admin
# from .models import Reservation

# @admin.register(Reservation)
# class ReservationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'date', 'number_of_people')
    

from home.models import Reservation

admin.site.register(Reservation)