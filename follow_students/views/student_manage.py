from django.views import View
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from follow_students.models import Student, Grade

class StudentManage(View):

    def get(self, request):

        students = Student.objects.all()
        grades = Grade.objects.all()
        return render(request, 'studentManage.html', {
            'students': students,
            'grades': grades
            })
    
    def post(self, request, *args, **kwargs):

        eliminate_student = Student.objects.get(id = request.POST['idStudent'])
        eliminate_student.delete()

        return redirect('studentManage')