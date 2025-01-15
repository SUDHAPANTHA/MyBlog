from blog_app import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
]