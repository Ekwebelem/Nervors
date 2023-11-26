from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'index.html')

def market(request):
    return render(request, 'market.html')

def partners(request):
    return render(request, 'partners.html')

def platform(request):
    return render(request, 'platform.html')

def tools(request):
    return render(request, 'tools.html')

def trading(request):
    return render(request, 'trading.html')

def openaccount(request):
    return render(request, 'openaccount.html')





def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form=UserCreationForm
    return render(request, 'registration/register.html', {'form':form})
