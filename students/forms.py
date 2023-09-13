from django import forms
from . models import Student

# Student registration
class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ('student_name', 'email','phone','address','student_code','course',)
        labels = {
            'student_name': 'Full Name',
            'email': 'Email',            
        }
        
        def __init__(self, *args, **kwargs):
            super(StudentForm, self).__init__(*args, **kwargs)
            self.fields['course'].empty_label = 'Select Course'