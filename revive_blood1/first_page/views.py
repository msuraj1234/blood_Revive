from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    try:
        user = request.session['user']
    except:
        user = ''
    if user:
        return render(request,'first_page/process.html')
    else:
        return HttpResponse("Can't Access")

def index1(request):
    return render(request,'first_page/about1.html')

def index2(request):
    return render(request,'first_page/contact1.html')

def index3(request):
    return render(request,'first_page/gallery1.html')

def index4(request):
    return render(request,'first_page/home1.html')