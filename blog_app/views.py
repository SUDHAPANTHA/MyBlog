from django.http import HttpResponseRedirect
from django.shortcuts import render

from blog_app.models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "post-detail.html", {"post": post})
def post_edit(request, id):
            post = Post.objects.get(id=id)
            if request.method == "GET":
                return render(request, "post-edit.html", {"post": post},)
            else:
                post.title = request.POST["title"]
                post.save()
                return HttpResponseRedirect("/")
def post_delete(request, pk):
    todo = Post.objects.get(id=pk)
    todo.delete()
    return HttpResponseRedirect("/")
