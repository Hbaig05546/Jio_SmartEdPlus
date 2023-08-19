from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from . import models

    
    
class SignupTeacherView(View):
    def get(self, request):
        return render(request, 'teacher_signup.html')
    
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password_confirm')
        sub_name = request.POST.get('sub_name')
        school_name = request.POST.get('school_name')
        
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('accounts:signup-teacher')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('accounts:signup-teacher')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('accounts:signup-teacher')
        
        user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname, email=email, password=password1)
        user.save()
        teacher = models.Teacher.objects.create(user=user,subject=sub_name,school_name=school_name)
        teacher.save()
        messages.success(request, "Account created successfully!")
        return redirect('accounts:login')
    
    
class SignupStudentView(View):
    def get(self, request):
        return render(request, 'student_signup.html')
    
    def post(self, request):
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password_confirm')
        school_name = request.POST.get('school_name')
        standard = request.POST.get('standard')
        
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('accounts:signup-student')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('accounts:signup-student')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('accounts:signup-student')
        
        user = User.objects.create_user(username=username, first_name=firstname,last_name=lastname, email=email, password=password1)
        user.save()
        student = models.Student.objects.create(user=user,standard=standard,school_name=school_name)
        student.save()
        messages.success(request, "Account created successfully!")
        return redirect('accounts:login')


class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:home')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('accounts:login')
        
class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:home')


class HomeView(View):
    template_name = 'base/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class OptionView(TemplateView):
    template_name = 'user_role.html'
