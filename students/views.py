from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Student
from . forms import StudentForm

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
    return render(request, 'Student_results/results.html')

def add_result(request):
    # result_form = ResultForm(request.POST)
    # if result_form.is_valid():
    #     # result_form.save()
        
    #     new_student_code = result_form.cleaned_data('student_code')
    #     new_course = result_form.cleaned_data('course')
    #     new_module_one = result_form.cleaned_data('module_one')
    #     new_module_two = result_form.cleaned_data('module_two')
    #     new_module_three = result_form.cleaned_data('module_three')
    #     new_module_four = result_form.cleaned_data('module_four')
    #     new_gpa = result_form.cleaned_data('gpa')
        
    #     new_results = Results(
    #         student_code = new_student_code,
    #         course = new_course,
    #         module_one = new_module_one,
    #         module_two = new_module_two,
    #         module_three = new_module_three,
    #         module_four = new_module_four,
    #         gpa = new_gpa          
    #     )
        
    #     new_results.save()
    #     return render(request, 'Student_results/add_result.html', {
    #             'result_form': ResultForm()              
    #         })        
    #     return HttpResponseRedirect(reverse('Student_results'))   
    # else:
    return render(request, 'Student_results/add_result.html')           
     
     

def about_view(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact.html')
        