from blog_app import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post-detail/<int:pk>/', views.post_detail, name='post-detail'),
    path('draft-list/<int:pk>/', views.draft_list, name='draft-list'),
    path('draft-detail/<int:pk>/', views.draft_detail, name='draft-detail'),
]





