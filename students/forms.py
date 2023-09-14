from django import forms
from . models import Student

# Student registration
class StudentForm(forms.ModelForm):
    
    student_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}) )
    
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}))
    
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}))
    
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}))
    
    student_code = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}))
    
    # course  = forms.CharField(widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}))
    
    
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
        
        
           