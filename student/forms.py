from django import forms
from.models import student_data,Teacher_data,img_upload

class student_form(forms.ModelForm):
    class Meta:
        model = student_data
        fields = ['name','enrollment_no','age','class_level']

class teacher_form(forms.ModelForm):
    class Meta:
        model = Teacher_data
        fields = ['name','subject','salary']

class img_form(forms.ModelForm):
    class Meta:
        model = img_upload
        fields = ['name','img']