from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  
import datetime

# Create your models here





# userprofile Model

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.username
        




# Contact Model

class Contact(models.Model):
    name = models.CharField(max_length=100, default="Default Name")
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=200, default="No Subject")

    message = models.TextField(blank=True, default="")

    def __str__(self):
        return f"{self.name} - {self.subject}"





# user_profile


class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',  # better folder name for uploads
        blank=True
    )


    def __str__(self):
        return self.user.username
    




# Reservation Model
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    number_of_people = models.PositiveIntegerField()
    special_request = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name  










class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
    

    from django.db import models

class Chef(models.Model):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chefs/')
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User_profile.objects.create(user=instance)
