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
    path('contact/', views.contact, name="contact"),

    # Team stuff
    path('team/', views.team, name="team"),
    path('add_team/', views.add_team, name="add-team"),

    # Appointment stuff
    path('add_appointment/', views.add_appointment, name="add_appointment"),
    path('show_appointment/<appointment_id>', views.show_appointment, name="show_appointment"),
    path('list_appointment/', views.list_appointment, name="list_appointment"),
    path('update_appointment/<appointment_id>', views.update_appointment, name="update_appointment"),
    path('delete_appointment/<appointment_id>', views.delete_appointment, name="delete_appointment"),

]