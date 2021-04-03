from django.urls import path, include
from .views import *
urlpatterns = [
    path('dashboard', dashboard),
    path('', index),
    path('login', login),
    path('signup', signup),
    path('mymemes', mymemes),
    path('forgot', forgot),
    path('notifications', notifications),
    path('developers', developers),
    path('contact', contact),
    path('search', search),

]