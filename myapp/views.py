from django.shortcuts import render ,redirect
from .models import Post
from .form import Comments
# Create your views here.

def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = Post.objects.filter(title__icontains=q)
    else:
        posts = Post.objects.all()
    return render (request , 'home.htm', {'posts' : posts})


def bpost(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request , 'post.htm',{'post':post})