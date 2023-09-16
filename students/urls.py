from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_view, name='about_us'),
    path('contact_us', views.contact_us, name='contact' ),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('student_registration', views.student_registration_form, name='student_registration'),
    path('<int:id>', views.student_registration_form, name='update'),
    path('delete<int:id>', views.remove_student, name='delete'),
    path('view<int:id>', views.view_student, name='view_student'),
]