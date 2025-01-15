from blog_app import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path("post_edit/<int:id>/", views.post_edit, name="post-edit"),
    path('post_delete/<int:pk>/', views.post_delete, name='post-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
