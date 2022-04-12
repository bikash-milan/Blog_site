
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate,logout
from matplotlib.style import context
from requests import delete
from portal.models import blog
from django.contrib.auth.decorators import login_required
# from djando.contrib.auth.models import User,auth
# Create your views here.

def index(request):
    print("hello world")
    return render(request,'index.html')

def register(request):
    if request.method =="POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
       
        if password1 == password2:
            user = User.objects.create(username=username)
            user.set_password(password1)
            user.save()
            print("user created")  
            return redirect('register')
            
        else:
            print("password not match")
        return redirect('/')
    else:
        return render(request,'register.html')

def Login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('myblog')  
        else:                
            return redirect('register')
    else:
        return redirect('register')

def myblog(request):
    posts = blog.objects.all()
    context = {'posts':posts}
    return render(request,'myblog.html',context)

def editblog(request):
    return render(request,'editblog.html')




# def myblog(request,pk):
#     posts = blog.objects.get(pk=pk)
#     context = {'posts':posts}
#     return render(request,'myblog.html', context)





def blog_details(request,id):
    edit = blog.objects.get(id=id)
    context = {'edit':edit}
    return render(request,'blog_details.html',context)


# def blog1(request,id):
#     edit = blog.objects.get(id=id)
#     context = {'edit':edit}
#     return render(request,'blog1.html',context)


# def blog1(request):
#     return render(request,'blog1.html')

@login_required(login_url='register')
def writeblog(request):
    if request.method =="POST":
        author = request.user
        title = request.POST['title']
        content = request.POST['content']
        desc = request.POST['desc']
        img = request.POST['img']

        blg = blog.objects.create(author=author,title=title,content=content,desc=desc,img=img)
        blg.save()
        return redirect('myblog')
    return render(request,'writeblog.html')


def Logout(request):

    logout(request)
    return redirect('index')


def delete_post(request,id):
    edit = blog.objects.get(id=id)
    edit.delete()
    return redirect('myblog')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

def info(request):
    return render(request,'info.html')


def editb(request,id):
    edit = blog.objects.get(id=id)
    if request.method=='POST':

        title = request.POST.get('title')
        content = request.POST.get('content')
        print(len(request.FILES))
        if len(request.FILES)!=0:
            img = request.FILES['img']
            edit.img = img
        desc = request.POST.get('desc')
        edit.title = title
        edit.content = content
        edit.desc = desc
        edit.save()
        return redirect('myblog')
    return render(request, 'editb.html',{'edit':edit})