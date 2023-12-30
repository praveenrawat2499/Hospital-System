
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from app.views import custom_logout
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment_form, name='appointment'),
    path('appointment-list/', views.appointment_list, name='appointment_list'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('feature/', views.feature, name='feature'),
    path('404/', views.Error_404, name='404'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('registration/', views.registration, name='registration'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('logout/', views.custom_logout, name='custom_logout'),
    
]
