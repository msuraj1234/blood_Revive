from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import Blood_donor_form
from django.conf import settings
from django.core.mail import send_mail
from donor_app.models import Donor_mdl
from .models import Blood_donor_model
from geopy.geocoders import Nominatim
import haversine as hs
from datetime import datetime, timedelta,date

# Create your views here.
def Receiver(request):
    if request.method == 'POST':
        fm=Blood_donor_form(request.POST)
        if fm.is_valid():
            Nm=fm.cleaned_data['Name']
            Pa=fm.cleaned_data['PatientAge']
            Pabg=fm.cleaned_data['PatientBloodGroup']
            Ubr=fm.cleaned_data['Unitsofbloodrequried']
            Pn=fm.cleaned_data['PhoneNumber']
            Em=fm.cleaned_data['Email']
            Hn=fm.cleaned_data['HospitalName']
            Ad=fm.cleaned_data['Address']
            ci=fm.cleaned_data['city']
            P=fm.cleaned_data['Purpose']
            data=Blood_donor_model(Email=Em,Name=Nm,PatientAge=Pa,PatientBloodGroup=Pabg,Unitsofbloodrequried=Ubr,PhoneNumber=Pn,HospitalName=Hn,Address=Ad,city=ci,Purpose=P)
            data.save()
            send_mail(
                f"Blood Revive",
                f"{Nm} !! Welcome !! WE got your request Details"
                f" Hope we provided you requried help!!"
                f" Thank YOu!",
                settings.EMAIL_HOST_USER,
                [Em]
                )
            request.session['Address'] = Ad
            request.session['PatientBloodGroup'] = Pabg
            fm = Blood_donor_form()
        # return render(request, 'receiver_app/receiver.html', {'fm': fm})
        return HttpResponseRedirect('/receiver/show')
    else:
        fm = Blood_donor_form()
        return render(request, 'receiver_app/receiver.html', {'fm': fm})


# Create your views here.
def show(request):
    serch_address = request.session['Address']
    geolocator = Nominatim(user_agent = 'http')
    try:
        location1 = geolocator.geocode(serch_address)
        x = (location1.latitude, location1.longitude)
    except:
        return HttpResponse('Location Cannot be found')
    how_many_days = 90
    date1 = Donor_mdl.objects.all().filter(LastDonateDate__lte=datetime.now()-timedelta(days=how_many_days),blood_group=request.session['PatientBloodGroup'])
    print(date1)
    all_radius = []
    for i in date1:
        print(i, geolocator.geocode(i.address))
        try:
            location2 = geolocator.geocode(i.address)
            y = (location2.latitude, location2.longitude)
        except:
            return HttpResponse('Location Cannot be found')
        z = "%.2f"%hs.haversine(x,y)
        all_radius.append([i.name,serch_address,i.address,i.blood_group,z+" km",i.phone_no])
    def Sort(sub_li):
        return(sorted(sub_li, key = lambda x: x[-1]))
    all_radius = Sort(all_radius)
    return render(request, 'receiver_app/showtable.html', {'group': all_radius})


