from django.urls import path
from . import views

urlpatterns = [
    path('receiver',views.Receiver,name='receiver'),
    path('show',views.show,name='show'),
]
