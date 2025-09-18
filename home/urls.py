from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


admin.site.site_header = "Restoran Admin"
admin.site.site_title = "Restoran Admin Portal"
admin.site.index_title = "Welcome to Restoran Portal"




urlpatterns = [
    path('', views.index, name='index'),  # Homepage view
    path('about/', views.about, name='about'),  # About page
    path('services/', views.services, name='services'),  # About page
    path('menu/', views.menu, name='menu'),  # Menu list page
    path('contact/', views.contact, name='contact'),  # Contact page
     path('booking/', views.booking, name='booking'),  # Contact page
    path('login/', views.login, name='login'),  # login page
    path('logout/', views.logout, name='logout'),#logout page
    path('register/', views.register, name='register'),#Register Page
    path('update-profile-picture/', views.profile_picture, name='update_profile_picture'),#profile_picture

     path('auth/', include('social_django.urls', namespace='social')),
   
]
