from django.urls import path
from . import views

urlpatterns = [
    path('portal/', views.show_portal_page, name='home'),
    path('portal/student/', views.show_students_page, name='student'),
    path('student/delete_student/<int:id>', views.delete_student_data, name='delete_student'),
    path('portal/teacher/', views.show_teachers_page, name='teacher'),
    path('teacher/delete_teacher/<int:id>', views.delete_teacher_data, name='delete_teacher'),
    path('img/', views.show_img_page, name='img')
]
