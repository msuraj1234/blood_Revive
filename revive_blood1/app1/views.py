from django.shortcuts import render
from django.contrib import messages
from .models import suggestion
from .forms import SuggestForm

# Create your views here.
def feeds(request):
    if request.method == 'POST':
        form = SuggestForm(request.POST)
        if form.is_valid():
            others = form.cleaned_data['others']
            name1 = form.cleaned_data['name1']
            email = form.cleaned_data['email']
            data = suggestion(others=others,email=email,name1=name1)
            data.save()
            form = SuggestForm()

        return render(request, 'app1/view.html', {'form':form})
    else:
        form = SuggestForm()
        return render(request, 'app1/view.html', {'form':form})
            
def facts(request):
    return render(request,'app1/blood_revive.html')