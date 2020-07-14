from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogCafe 
from django.utils import timezone

def home(request):
    blogs = BlogCafe.objects
    return render(request,'home.html',{'blogs' : blogs})

def detail(request, blog_id) :
    blogdetail = get_object_or_404(BlogCafe, pk=blog_id)
    return render(request, 'detail.html', {'blogdetail' : blogdetail })

def new(request):
    return render(request,'new.html')

def create(request):
    blog = BlogCafe()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def jinsu(request):
    return render(request,'jinsu.html')

def seunghwa(request):
    return render(request,'seunghwa.html')

def blog(request):
    return render(request,'blog.html')
