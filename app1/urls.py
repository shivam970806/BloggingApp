from django.urls import path
from app1 import views
urlpatterns = [
    path('', views.index, name='Home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('myform', views.myform, name='My Form'),
    path('postmethod', views.postdata, name='Post Method'),
    path('login', views.loginpage, name='Login form'),
    path('logout', views.logout, name='Logout form'),
    path('registration', views.reg, name='form'),
    path('blog', views.blog, name='blog'),
    path('blogs', views.blogs, name='blogs'),
    path('blogsdetails', views.blogsdetails, name='blogsdetails'),
    # path('blogspkdetails', views.blogspkdetails, name='blogspkdetails'),
    path('blogtable', views.blogtable, name='blogtable'),
    path('editblog', views.editblog, name='editblog'),
    path('deleteblog', views.deleteblog, name='deleteblog'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('blog_new', views.blog_new, name='blog_new'),
    path('user_dashboard', views.user_dashboard, name='user_dashboard'),
    # path('hasno_blog', views.hasno_blog, name='hasno_blog'),


]

