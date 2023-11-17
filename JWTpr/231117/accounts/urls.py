from django.contrib import admin
from django.urls import path, include
from .views import example_view
from . import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('test/', example_view),
    path('join/', include('dj_rest_auth.registration.urls')),
    path('mypage/', views.getmypage, name='mypage'),
]