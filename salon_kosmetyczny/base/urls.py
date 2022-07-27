from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),

    # Navbar links
    path('treatments/', views.treatments, name="treatments"),
    path('prices/', views.prices, name="prices"),
    path('reviews/', views.reviews, name="reviews"),
    path('sale/', views.sale, name="sale"),
    path('training/', views.training, name="training"),
    path('team/', views.team, name="team"),
    path('contact/', views.contact, name="contact"),
    path('appointment/', views.appointment, name="appointment"),

]