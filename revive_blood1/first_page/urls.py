from django.urls import path
from . import views

urlpatterns = [
    path('login',views.index, name = 'process'),
    path('about1',views.index1, name = 'about1'),
    path('contact1',views.index2, name = 'contact1'),
    path('gallery1',views.index3, name = 'gallery1'),
    path('home1',views.index4, name = 'home1'),
]