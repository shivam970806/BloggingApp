from django.contrib import messages, auth
from django.contrib.auth import authenticate, login as login1,get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app1.models import Register, Blog, Contact


def index(request):
    blog = Blog.objects.all()
    return render(request, 'index.html',{'blogs': blog})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        n = request.POST['name']
        e = request.POST['email']
        s = request.POST['subject']
        m = request.POST['message']
        #user already exists or not
        if Contact.objects.filter(email=e).exists():
            messages.info(request, 'This user already exists')
            return redirect('/contact')

        elif Contact.objects is None:
            messages.info(request, 'Please filled details')
            return redirect('/contact')
        else:
            #save inside  Register table
            c1 = Contact.objects.create(name=n, email=e, subject=s, message=m)
            c1.save()
            messages.info(request, 'Data sent successfully')
            return redirect('/contact')
    else:
        return render(request, 'contact.html')

def myform(request):
    if request.method == "GET":
        name = request.GET['n']
        email = request.GET['e']
        #print(name)
        #print(email)
        return render(request, 'contact.html', {'n': name, 'e': email})


def postdata(request):
    if request.method == "POST":
        name = request.POST['n']
        email = request.POST['e']
        #print(name)
        #print(email)
        return render(request, 'output.html', {'n': name, 'e': email})
    else:
        return render(request, 'postdata.html')


#*************************************************************************************

#registration form-----
def reg(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        print(firstname)
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        
        #user already exists or not
        if User.objects.filter(email=email).exists():
            messages.info(request, 'This user already exists')
            return redirect('/registraion')
        else:
            #save inside  Register table
            form1 = User.objects.create_user(first_name=firstname, last_name=lastname,username=username,password=password1,email=email )
            form1.save()
            messages.info(request, 'Data saved successfully')
            return redirect('/registration')
    else:
        return render(request, 'registration.html')

#***********************************************************************************
"""
def login(request):
    if request.method == "POST":
        uname = request.POST['e']
        upass = request.POST['p']
        user = auth.authenticate(username=uname, password=upass)
        print(user)
        print(user.username)
        print(user.email)
        #print(user.get_full_name)
        if user is not None:
            if user.is_active:
                login1(request, user)
                # Redirect to a success page.
                return redirect("/")
            else:
                return redirect("/login")
        # Return a 'disabled account' error message
        else:
            return redirect("/login")
    else:
        return  render(request, "login.html")

"""


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is None:
            user_queryset = User.objects.filter(email=username)
            if user_queryset:
                username = user_queryset[0].username
                user = authenticate(username=username, password=password)
        if user is not None:
            login1(request, user)
            # Redirect to a success page.
            return redirect('Home')

        # Return a 'disabled account' error message
        else:
            messages.info(request, "username and password is incorrect.")
            return render(request, "login.html")
    else:
        return render(request, "login.html")


def logout(request):
    #login or logout are bydefault a keyword
    from django.contrib.auth import logout as logout1
    logout1(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')


def blog(request):
    if request.method == "POST":
        
        title = request.POST['title']
        image = request.POST['image']
        description = request.POST['description']
        heading = request.POST['heading']
        #save inside  Register table
        # user_id = request.user.id
        # print(user_id)
        blog = Blog.objects.create(title=title, heading=heading,image=image, description=description)
        blog.save()
        messages.info(request, 'Data saved successfully')
        return redirect('/blog')
    else:
        return render(request, 'blog.html')


def blogs(request):
    blog = Blog.objects.all()
    return render(request,'blogs.html',{'blogs': blog})


def blogsdetails(request):
    blogid=request.GET.get('blogid')
    blog = Blog.objects.filter(pk=blogid)
    return render(request, 'blogsdetail.html', {'blogs': blog})


def blogtable(request):
    # blog = Blog.objects.all()
    # user = request.user.id
    blog = Blog.objects.filter(user_pk=request.user.id)
    print(blog)
    return render(request, 'blog_tble.html', {'blogs':blog})

#***********************************************************************************


def editblog(request):
    blogid=request.GET['blogid']
    blog = Blog.objects.filter(pk=blogid)
    if request.method == "POST":
        bid = request.POST['bid']
        title = request.POST['title']
        heading = request.POST['heading']
        description = request.POST['description']
        Blog.objects.filter(id=bid).update(title=title, heading=heading, description=description)
        return redirect('/blogs')
    else:
        blogid = request.GET['blogid']
        blog = Blog.objects.filter(id=blogid)
        return render(request, 'editblog.html', {'blogs': blog})

def editprofile(request):
   return render(request, 'editprofile.html')

def blog_new(request):
    return render(request, 'new_page.html')

def user_dashboard(request):
    blog = Blog.objects.all()
    return render(request, 'user_dashboard.html',{'blogs': blog})

def deleteblog(request):
    bid = request.GET['bid']
    print(bid)
    Blog.objects.filter(id=bid).delete()
    return redirect("/blogs")
