from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            # maybe to home
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'username or password is incorrect.'})   
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    # TODO Need to route to homepage
    # and dont forget to logout 
    return render(request, 'accounts/logout.html')