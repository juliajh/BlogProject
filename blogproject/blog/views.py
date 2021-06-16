from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth

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
    blog=Blog()
    blog.title=request.POST.get('title',False)
    blog.body=request.POST.get('body',False)
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')

def edit(request, id):
    edit_blog=Blog.objects.get(id=id)
    return render(request,'edit.html',{'blog':edit_blog})

def update(request, id):
    update_blog=Blog.objects.get(id=id)
    update_blog.title=request.POST.get('title',False)
    update_blog.body=request.POST.get('body',False)
    update_blog.pub_date=timezone.datetime.now()
    update_blog.image=request.POST.get('image','')
    update_blog.save()
    return redirect('detail',update_blog.id)

'''
def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request.user)
            return redirect('home')
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'username or password is incorrect.'})
    return render(request,'login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        redirect('home')
    return render(request,'login.html')
'''