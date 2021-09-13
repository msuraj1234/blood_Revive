from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import Signup_form
from .forms import Login_form
from .models import Signup, Login
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def home(request):
    return render(request, 'users/home.html')


def about(request):
    return render(request, 'users/about.html')


def gallery(request):
    return render(request, 'users/gallery.html')


def contact(request):
    return render(request, 'users/contact.html')


def donation_process(request):
    return render(request, 'users/donation_process.html')


def signup(request):
    x=Signup.objects.all()

    if request.method == 'POST':
        fm = Signup_form(request.POST)
        print(fm.is_valid())
        if fm.is_valid():
            fn = fm.cleaned_data['first_name']
            ln = fm.cleaned_data['last_name']
            m = fm.cleaned_data['mobile']
            e = fm.cleaned_data['email']
            for i in x:
                if e in i.email:
                    msg = 'Email already exists'
                    return render(request, 'users/signup.html', {'form': fm, 'msg': msg})
            p = fm.cleaned_data['password']
            rp = fm.cleaned_data['repeat_password']
            sng = Signup(first_name=fn, last_name=ln, mobile=m, email=e, password=p, repeat_password=rp)
            sng.save()
            fm = Signup_form()
            msg = 'Your have successfully registered'
            return render(request, 'users/signup.html', {'form': fm, 'msg': msg})

    else:
        fm = Signup_form()
    sng = Signup.objects.all()
    return render(request, 'users/signup.html', {'form': fm, 's': sng})



def user_login(request):
    if request.method == "POST":
        fm = Login_form(request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['email_id']
            upass = fm.cleaned_data['password']
            try:
                user = Signup.objects.get(email=uname,password=upass)
            except:
                return HttpResponse('not found')
            if user is not None:
                request.session['user'] = uname
                messages.success(request, 'Logged in successfully !!')
                return HttpResponseRedirect('login/login')
    else:
        fm = Login_form()
    return render(request, 'users/login.html', {'form': fm})




    # email_id = request.POST.get('email_id')
    # password = request.POST.get('password')
    # user = authenticate(request,email_id=email_id,password=password)
    # if user is not None:
    #     login(request,email_id)
    #     redirect('home')
    #     context = {}

    # return render(request,'userapp/login.html',context)


from django.shortcuts import render


# Create your views here.
def user_logout(request):
    del request.session['user']
    return HttpResponseRedirect('/login')
