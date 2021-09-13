import string
import random
from django.conf import settings
from django.core.mail import send_mail
from django.http import response
from django.shortcuts import render
from .forms import Donor_frm
from .models import Donor_mdl


def donor(request):
    if request.method == 'POST':
        fm = Donor_frm(request.POST)
        print(fm.is_valid())
        if fm.is_valid():
            donation_id = int(''.join(random.choice(string.digits) for n in range(4)))
            name = fm.cleaned_data['name']
            fname = fm.cleaned_data['fname']
            blood_group = fm.cleaned_data['blood_group']
            age = fm.cleaned_data['age']
            if age<=16:
                message='Ur Age not sufficient For Donating Blood'
                return render(request, 'Donor.html', {'forms': fm,'message':message})
            else:
                Gender = fm.cleaned_data['Gender']
                date_brth = fm.cleaned_data['date_brth']
                email = fm.cleaned_data['email']
                address = fm.cleaned_data['address']
                city = fm.cleaned_data["city"]
                phone_no = fm.cleaned_data['phone_no']
                LastDonateDate = fm.cleaned_data['LastDonateDate']
                extra_info = fm.cleaned_data['extra_info']
                reg = Donor_mdl(donation_id=donation_id, name=name, fname=fname,blood_group=blood_group, age=age, Gender=Gender, date_brth=date_brth,
                                  email=email, address=address, city=city, phone_no=phone_no, LastDonateDate=LastDonateDate, extra_info=extra_info,)
                reg.save()
                send_mail(
                f"Blood Revive",
                f"{name} !! your are a saviour WE got UR registerd Details"
                f" WE get back When we need UR presence!!"
                f" Thank YOu!",
                settings.EMAIL_HOST_USER,
                [email]
                )
                fm = Donor_frm()
                msg = 'FORM SUCCESSFULLY SUBMITTED!!'
        return render(request, 'donor_app/Donor.html', {'forms': fm, 'msg': msg})
    else:
        fm = Donor_frm()
        data = {'forms': fm}
        return render(request,'donor_app/Donor.html',data)

