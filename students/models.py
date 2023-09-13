from django.db import models

# Create your models here.
# course model
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_period = models.CharField(max_length=10)
    tuition = models.FloatField()
    
    def __str__(self):
        return self.course_name
    
# Student table / model
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    student_code = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student_name}  {self.course}"