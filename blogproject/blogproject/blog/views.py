from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
from account.forms import RegisterForm
from django.contrib import messages

# Create your views here.
def home(request):
    blogs=Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})

def aboutme(request):
    return render(request,'aboutme.html')

def bloglist(request):
    blogs=Blog.objects.all()
    return render(request,'bloglist.html',{'blogs':blogs})

def new(request):
    return render(request,'new.html')

def create(request):
    if request.user.is_authenticated:
        blog=Blog()
        blog.title=request.POST.get('title',False)
        blog.body=request.POST.get('body',False)
        blog.pub_date=timezone.datetime.now()
        if 'image' in request.FILES:
            blog.image=request.FILES['image']
        blog.writer=request.user
        blog.save()
        return redirect('/blog/'+str(blog.id))
    else:
        return redirect('bloglist')

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    if delete_blog.writer == request.user:
        delete_blog.delete()
    return redirect('bloglist')

def edit(request, id):
    edit_blog=Blog.objects.get(id=id)
    return render(request,'edit.html',{'blog':edit_blog})

def update(request, id):
    update_blog=Blog.objects.get(id=id)
    update_blog.title=request.POST.get('title',False)
    update_blog.body=request.POST.get('body',False)
    update_blog.pub_date=timezone.datetime.now()
    if 'image' in request.FILES:
        update_blog.image=request.FILES['image']
    update_blog.writer=request.user
    update_blog.save()
    return redirect('detail',update_blog.id)
