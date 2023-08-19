from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Assignment)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Enrollment)
