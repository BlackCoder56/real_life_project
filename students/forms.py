from django import forms
from . models import Student, Result

# Student registration
class StudentForm(forms.ModelForm):
    
    student_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}) )
    
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}))
    
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}))
    
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}))
    
    student_code = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "placeholder": "eg. 'ST412'","class": "form-control rounded", "name":"student_code", "maxlength":"5","pattern":"ST[4-5][0-9][0-9]","title":"Enter correct format(Between ST400-ST600)"}))
    
   
    
    
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
        

class ResultForm(forms.ModelForm): 
   
    student_code = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Student Code", "class": "form-control rounded"}),
                                 label="")
    student_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Student Name", "class": "form-control rounded"}), label="")
    m_one = forms.IntegerField(required=True,
                              widget=forms.widgets.TextInput(attrs={"class": "form-control rounded", "placeholder":"Module one"}),
                              label="")
    m_two = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded", "placeholder":"Module two"}),
                              label="")
    m_three = forms.IntegerField(required=True,widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}),
                              label="")
    m_four = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}),
                           label="")
    gpa = forms.FloatField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control rounded"}),     label="")
    
    
    class Meta:
        model = Result
        fields = ('student_code', 'student_name', 'm_one', 'm_two', 'm_three', 'm_four', 'gpa')
        
    def __init__(self, *args, **kwargs):
        super(ResultForm, self).__init__(*args, **kwargs)
        



        
        
        
           