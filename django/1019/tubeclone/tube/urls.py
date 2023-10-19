from django.urls import path
from . import views

app_name = 'tube'  # {% url 'tube:post_list' %} 또는 {% url 'tube:post_detail' post.pk %} 이런식으로 쓰기 위해 필요함


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/comment/new', views.comment_new, name='comment_new'),
]