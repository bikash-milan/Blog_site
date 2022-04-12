
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.Login,name='login'),
    path('myblog',views.myblog,name='myblog'),
    # path('blog1',views.blog1,name='blog1'),
    path('writeblog',views.writeblog,name='writeblog'),
    path('myblog/<int:id>',views.myblog,name='readblog'),
    path('editblog',views.editblog,name='editblog'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('service',views.service,name='service'),
    path('info',views.info,name='info'),
    path('blog_details/<int:id>',views.blog_details,name='blog_details'),
    path('blog_details/delete_post/<int:id>',views.delete_post,name='delete_post'),
    path('blog_details/editb/<int:id>',views.editb,name='editb')
   

    # path('login',views.Login,name='login'),
    # path('logout',views.Logout,name='logout')
]
 
