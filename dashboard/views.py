from django.shortcuts import render

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# from .models import
# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard/index.html', {'dashboard': dashboard})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('dashboard'))

# def user_login(request):
#     if request == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username,password=password)
#         if user:
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('dashboard'))
#             else:
#                 return HttpResponse("Account not Active")
#         else:
#             print("Someone tried to login and failed")
#             print("Username:{} and password {}".format(username,password))
#             return HttpResponse("Invalid login dailes supplied!")

#     else:
#         return render(request, 'dashboard/page-login.html', {'login_user': login_user})