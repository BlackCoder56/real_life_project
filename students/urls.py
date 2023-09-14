from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_view, name='about_us'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('student_registration', views.student_registration_form, name='student_registration'),
    path('<int:id>', views.student_registration_form, name='update'),
]