
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='basic'),
    path('about_us/',views.About, name='about_us'),
    path('do_not_click/',views.Dont, name='do_not_click'),
    #path('contact/',views.Contact, name='contact'),
    #path('signup/',views.Signup, name='signup'),
    path('',include('signup.urls')),
    path('',include('login.urls')),
    path('',include('contact.urls')),
    path('',include('calculate_cost.urls')),
    #path('login/',views.Login,name='login'),
    path('activate_pincode/',views.Activate_Pincode,name='activate_pincode'),
    path('pricing_know_more/',views.Pricing_Know_More,name='pricing_know_more'),
    path('track_order/',views.Track_Order,name='track_order'),
    path('demo/',views.Demo,name='demo'),
    #path('register/',views.register,name='register'),
    # path('calculate_cost/',views.calculate_cost,name='calculate_cost'),

    #path('about_us/',TemplateView.as_view(template_name='about_us.html'))
]
