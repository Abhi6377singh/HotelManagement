"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customer.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',index_view, name="index"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('about/', about_view, name="about"),
    path('service/', service_view, name="service"),
    path('service/', service_view, name="service"),
    path('contact/', contact_view, name="contact"),
    path('otp/', otp_view, name="otp"),
    path('logout/', logout_view, name="logout"),
    # path('hotel_detail/', hotel_detail_view, name="hotel_detail"),
    path('room_list/', room_list, name="room_list"),
    path('book_room/<int:room_id>', book_room, name="book_room"),
    
    path('book_room/<int:room_id>/paymenthandler/', paymenthandler, name='paymenthandler'),
]

