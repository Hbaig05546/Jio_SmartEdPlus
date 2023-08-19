from django.shortcuts import render, redirect
from django.views.generic import View,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Student,Teacher
from .models import *
from django.http import Http404


class CourseListView(LoginRequiredMixin, ListView):
    template_name = 'courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        user = self.request.user
        if Student.objects.filter(user=user).exists():
            queryset = Enrollment.objects.filter(student__user=user).select_related('course')
            print(queryset)
            return [enrollment.course for enrollment in queryset]
        elif Teacher.objects.filter(user=user).exists():
            teacher = Teacher.objects.get(user=user)
            queryset = Course.objects.filter(owner=teacher).order_by('name')
            print(queryset)
            return queryset
        else:   
            return Course.objects.none()
        
class AddCourseView(LoginRequiredMixin,View):

    def get(self,request):
        if not Teacher.objects.filter(user = self.request.user):
            print("==========not a teacher=============")
            raise Http404("Not Authorised")
        return render(request,'add_course.html')

    def post(self, request):
        # Get course details from form data
        print(request.POST)
        course_name = request.POST.get('name')
        course_description = request.POST.get('description')

        # Create new course object
        course = Course(name=course_name, description=course_description,owner = self.request.user.teacher)
        course.save()

        # Get lesson details from form data
        lesson_count = int(request.POST.get('lesson-count'))
        for i in range(1, lesson_count):
            lesson_name = request.POST.get(f'lesson-name-{i}')
            lesson_description = request.POST.get(f'lesson-description-{i}')
            lesson_content = request.POST.get(f'lesson-file-{i}')
            print(lesson_content)
            # Create new lesson object and add it to course
            lesson = Lesson(name=lesson_name, description=lesson_description, course=course,content = lesson_content)
            print(lesson.content)
            lesson.save()

        return redirect('courses:all')
    
class CourseView(LoginRequiredMixin,DetailView):
    model = Course
    template_name = 'course_detail.html'
    