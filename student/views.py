from django.shortcuts import render,redirect
from .forms import student_form,teacher_form,img_form
from .models import student_data,Teacher_data

# Create your views here.
def show_portal_page(request):
    return render(request,'portal.html')

def show_students_page(request):
    students = student_data.objects.all()
    if request.method=='POST':
        form = student_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = student_form()
    context = {
        'form':form,
        'students':students
    }
    return render(request,'student.html',context)

def delete_student_data(request,id):
    del_students = student_data.objects.get(id=id)
    del_students.delete()
    return redirect('student')

def show_teachers_page(request):
    teachers = Teacher_data.objects.all()
    if request.method=='POST':
        form = teacher_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher')
    else:
        form = teacher_form()
    context = {
        'form':form,
        'teachers':teachers
    }
    return render(request,'teacher.html',context)

def delete_teacher_data(request,id):
    del_teachers = Teacher_data.objects.get(id=id)
    del_teachers.delete()
    return redirect('teacher')

def show_img_page(request):
    if request.method=='POST':
        form = img_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('img')
    else:
        form = img_form()
        return render(request,'img_page.html',{'form':form})