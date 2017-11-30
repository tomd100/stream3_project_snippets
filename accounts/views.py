from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import auth, messages
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required


#-------------------------------------------------------------------------------

def home_page(request):
    return render(request, 'index.html')
    
#-------------------------------------------------------------------------------

def logout(request):
    auth.logout(request);                                                      
    messages.success(request, "You have successfully logged out")
    return redirect(home_page);
    
#-------------------------------------------------------------------------------

def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user);
                messages.success(request, "You have successfully logged in")
                return redirect(home_page)
            else:
                # messages.warning(request, "Your user name or password was not recognised ")
                form.add_error(None, "Your user name or password was not recognised ")
    else:
        form = UserLoginForm();
    return render(request, "login.html", {"form": form})    
    
#-------------------------------------------------------------------------------    
