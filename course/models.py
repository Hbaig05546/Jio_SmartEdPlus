from django.db import models
from accounts.models import Teacher,Student
from django.core.validators import FileExtensionValidator


video_extensions = ['.mp4', '.mov', '.avi', '.wmv', '.mkv', '.flv']
photo_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg']
pdf_extensions = ['.pdf']
document_extensions = ['.doc', '.docx', '.txt', '.rtf', '.odt', '.wps']
presentation_extensions = ['.ppt', '.pptx', '.odp', '.key']
csv_extensions = ['.csv']
text_extensions = ['.txt']

EXTENSIONS = ['.mp4', '.mov', '.avi', '.wmv', '.mkv', '.flv','.jpg','.pdf', '.jpeg', '.png', '.gif', '.bmp', '.svg','.doc', '.docx', '.txt', '.rtf', '.odt', '.wps','.ppt', '.pptx', '.odp', '.key','.cvs','.txt']


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    content = models.FileField(blank=True,upload_to = 'content/',validators=[FileExtensionValidator(allowed_extensions=EXTENSIONS)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Assignment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Question(models.Model):
    text = models.TextField()
    answer = models.TextField()
    points = models.IntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.name}"

