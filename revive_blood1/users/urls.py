from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('donation_process',views.donation_process,name='donation_process'),
    path('signup', views.signup,name='signup'),
    path('login',views.user_login,name='login'),
    path('logout', views.user_logout, name='logout')

]