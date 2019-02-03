from django.contrib import admin
from django.urls import path, include
from bookingapp.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookingapp/',include('bookingapp.urls')),
]
