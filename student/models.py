from django.db import models

# Create your models here.
#  Add a Teacher model with fields name, subject, and salary, and create relationships with the Student model
# Define a Student model with fields like name, age, class_level, and enrollment_date.

class student_data(models.Model):
    name = models.CharField(max_length=255)
    enrollment_no = models.BigIntegerField(unique=True)
    age = models.IntegerField()
    class_level = models.IntegerField()
    enrollment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Teacher_data(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    salary = models.IntegerField()
    def __str__(self):
        return self.name

class img_upload(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name