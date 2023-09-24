from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Student, Result
from . forms import StudentForm, ResultForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
# home view is views when logged in and it displays students in the system
def home(request):
    students = Student.objects.all()
    if request.user.is_authenticated:    
        return render(request, 'wisdom_academy/home.html', {'students': students})
    else:
         if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                # messages.success(request, 'You have successfully logged in!')
                return redirect('home')
            else:
                messages.error(request, 'An error occurred please try again!')
                return redirect('home')
    return render(request, 'wisdom_academy/home.html',{'students': students})
            
 
def signout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('index')
   

def signup(request):
    return render(request, 'wisdom_academy/signup.html')

def student_registration_form(request, id=0): 
        
    if request.user.is_authenticated:        
        if request.method == "GET":
                if id == 0:
                    form = StudentForm()
                else:
                    student = Student.objects.get(pk=id)
                    form = StudentForm(instance=student)
                return render(request, 'wisdom_academy/student_registration.html',{'form':form})
        else:                
        
            if id == 0:
                form = StudentForm(request.POST)
            else:
                student = Student.objects.get(pk=id)
                form = StudentForm(request.POST, instance=student)
            
            if form.is_valid():
                form.save()           
                return redirect('home')
            return render(request, 'wisdom_academy/student_registration.html',{'form':form})
    else:
        messages.success(request, 'An error occurred. Please try again!')
        return redirect('student_registration')
    
def remove_student(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('home')

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home'))
    
   
    # return redirect('home')
    # return render(request, 'wisdom_academy/student_registration.html',{})

# def view_student(request):
#     if request.user.is_authenticated:
#         students = Student.objects.all()
#         return render(request, 'home.html', {'students': students})
#     else:
#         messages.success(request, 'You have to be logged to view students!')
#         return redirect('home', {'students': students})


def result_home(request):
    results = Result.objects.all()
    if request.user.is_authenticated:
        return render(request, 'Student_results/results.html', {'results':results})
    else:
        return redirect('home')        

def add_result(request, id=0):
    if request.user.is_authenticated:        
        if request.method == "GET":
            if id == 0:
                form = ResultForm()
            else:
                result = Result.objects.get(pk=id)
                form = ResultForm(instance=result)
            return render(request, 'Student_results/add_result.html',{'form':form})
        else:                
        
            if id == 0:
                form = ResultForm(request.POST)
            else:
                result = Result.objects.get(pk=id)
                form = ResultForm(request.POST, instance=result)            
            if form.is_valid():
                form.save()           
                return redirect('Student_results')
            return render(request, 'Student_results/add_result.html', {'form':form})
    else:
        messages.success(request, 'An error occurred. Please try again!')
        return redirect('add_results')
    
def tuition_view(request):
    return render(request, 'Student_tuition/tuition.html')

def remove_result(request, id):
    results = Result.objects.get(pk=id)
    results.delete()
    return redirect('Student_results')

def view_result(request, id):
    results = Result.objects.get(pk=id)
    return HttpResponseRedirect(reverse('Student_results'))

def about_view(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact.html')
        