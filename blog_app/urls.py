from blog_app import views
from django.urls import path



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post-detail/<int:pk>/', views.post_detail, name='post-detail'),
    path("post_edit/<int:id>/", views.post_edit, name="post-edit"),
    path('post_delete/<int:pk>/', views.post_delete, name='post-delete'),
    path('draft_list/<int:pk>/', views.draft_list, name='draft_list'),
    path('draft_detail/<int:pk>/', views.draft_detail, name='draft_detail'),
]


