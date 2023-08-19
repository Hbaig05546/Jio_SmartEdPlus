from django.urls import path,include
from .views import *
app_name = 'courses'


urlpatterns = [
    path('all/', CourseListView.as_view(),name='all'),
    path('add-course/', AddCourseView.as_view(),name='add-course'),
    path('course/<int:pk>', CourseView.as_view(),name='course'),
]
