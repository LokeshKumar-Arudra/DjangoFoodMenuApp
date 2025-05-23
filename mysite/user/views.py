from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)  #here request.POST is used to fetch data from form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm() # this renders an empty form
    return render(request,'user/register.html',{'form': form})

def logout_view(request):
    logout(request)
    return render(request,'user/logout.html')

@login_required
def profilepage(request):   # the request object and the request object contains the currently logged in user.
    return render(request,'user/profilepage.html')


