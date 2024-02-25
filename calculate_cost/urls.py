from django.urls import path,include
from . import views

urlpatterns=[
    path('calculate_cost/',views.calculate_cost,name='calculate_cost')
]