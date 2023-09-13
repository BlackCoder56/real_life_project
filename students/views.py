from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Student
from . forms import StudentForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')
        else:
            messages.error(request, 'An error occurred please try again!')
            return redirect('home')
    else:
         return render(request, 'wisdom_academy/home.html',{})
            
 
def signout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('index')
   

def signup(request):
    return render(request, 'wisdom_academy/signup.html')

def student_registration_form(request):
   
    form = StudentForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Registered a Student!')
            return redirect('home')
        return render(request, 'wisdom_academy/student_registration.html',{'form':form})
    else:
        messages.success(request, 'An error occurred. Please try again!')
        return redirect('home')
   
    # return redirect('home')
    # return render(request, 'wisdom_academy/student_registration.html',{})

def view_student(request):
    pass