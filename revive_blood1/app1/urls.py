from django.urls import path
from . import views

urlpatterns = [
    path('suggest', views.feeds, name = 'suggest'),
    path('facts', views.facts, name = 'facts'),

]