from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), # accounts/login
    path('logout/', views.logout, name='logout'), # accounts/logout
    path('signup/', views.signup, name='signup'),
]