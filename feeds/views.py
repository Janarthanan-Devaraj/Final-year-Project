from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


def index(request):
    return HttpResponse("<h1>hello World!!!</h1>")


def posts(request):
    posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-dateTime')
    return render(request, "feeds/posts.html", {'posts':posts})



@login_required(login_url = '/login')
def addPost(request):
    if request.method=="POST":
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feeds:posts')
    else:
        form=PostForm()
    return render(request, "feeds/add_post.html", {'form':form})