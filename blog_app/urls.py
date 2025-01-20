from django.urls import path

from blog_app import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="post-list"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view, name="post-detail"),
    path("draft-list/", views.DetailView.as_view, name="draft-list"),
    path("draft-detail/<int:pk>/", views.DraftDetailView.as_view, name="draft-detail"),
    path("post-create", views.post_create, name="post-create"),
    path("post-update/<int:pk>/", views.post_update, name="post-update"),
    path("post-delete/<int:pk>/", views.post_delete, name="post-delete"),
    path("draft-publish/<int:pk>/", views.draft_publish, name="draft-publish"),
    
  
]