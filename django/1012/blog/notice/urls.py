from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice, name='notice'),
    path('<int:pk>/', views.secretpost, name='secretpost'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]