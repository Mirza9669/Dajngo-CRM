from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(req):
    if req.method == 'POST':
        username = req.POST['Username']
        passwd = req.POST['Password']

        user = authenticate(req, username= username, password= passwd)
        if user is not None:
            login(req, user)
            messages.success(req, 'You have been Logged In!')
            return redirect('home')
        else:
            messages.success(req, "There was an error Logging in. Please Try Again")
            return redirect('home')
    else:
        return render(req, 'home.html', {})

def logout_user(req):
    logout(req)
    messages.success(req, "You have been Logged Out...")
    return redirect('home')

def register_user(req):
    return render(req, 'register.html', {})
