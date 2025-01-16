from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog_app.models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by("-published_at") #yesley chai publish vako data matra dekhaunxa and descending order ma aunxa latest vala post
    return render(request, "post_list.html", {"posts": posts})
def post_detail(request, pk):
    post = Post.objects.get(pk=pk, published_at__isnull=False)
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
@login_required
def draft_detail(request, pk):
    post = Post.objects.get(id=pk, published_at__isnull=True)
    return render(request, "draft_detail.html", {"post": post})
@login_required
def draft_list(request, pk):
    post = Post.objects.filter(id=pk, published_at__isnull=True)
    return render(request, "draft_list.html", {"post": post})


