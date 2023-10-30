from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignupForm
from .form import AddRecordForm
from .models import Record

# Create your views here.
def home(req):
    records = Record.objects.all()

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
        return render(req, 'home.html', {'records':records})

def logout_user(req):
    logout(req)
    messages.success(req, "You have been Logged Out...")
    return redirect('home')

def register_user(req):
    if req.method == 'POST':
        form = SignupForm(req.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            passwd = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = authenticate(username= username, password= passwd)
            login(req, user)
            messages.success(req, 'You have been succesfully Registered, Welcome!')
            return redirect('home')
    else:
        form = SignupForm()
        return render(req, 'register.html', {'form': form})
    
    return render(req, 'register.html', {'form': form})

def customer_record(req, pk):
    if req.user.is_authenticated:
        customer_record = Record.objects.get(id= pk)
        return render(req, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(req, "You are not Logged In")
        return redirect('home')
    
def add_record(req):
    form = AddRecordForm(req.POST or None)
    if req.user.is_authenticated:
        if req.method == 'POST':
            if form.is_valid:
                add_record = form.save()
                messages.success(req, 'Record Added')
                return redirect('home')
        else:
            return render(req, 'add_record.html', {'form': form})
    else:
        messages.success(req, 'You are not Logged In')
        return redirect('home')
    
def delete_record(req, pk):
    if req.user.is_authenticated:
        delete_it = Record.objects.get(id= pk)
        delete_it.delete()
        messages.success(req, "Customer Record is deleted")
        return redirect('home')
    else:
        messages.success(req, "You are not Logged In")
        return redirect('home')

def update_record(req, pk):
    if req.user.is_authenticated:
        current_record = Record.objects.get(id= pk)
        form = AddRecordForm(req.POST or None, instance= current_record)

        if form.is_valid():
            form.save()
            messages.success(req, "Customer Record is Updated")
            return redirect('home')
        else:
            return render(req, 'update_record.html', {'form': form})
    else:
        messages.success(req, "You are not Logged In")
        return redirect('home')
