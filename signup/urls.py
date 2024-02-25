from django.urls import path,include
from . import views

urlpatterns=[
    # path('signup/',views.signup,name='signup'),
    path('register/',views.register,name='register'),

]