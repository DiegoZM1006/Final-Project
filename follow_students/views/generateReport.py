from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from follow_students.models import Student, Consult, Grade, RegisNonAcademicActivity, Scholarship_expense

class GenerateReport(View):
    def post(self, request):
        selected_students = []
        student_ids = request.POST.getlist('selected_students')       
        for student_id in student_ids:
            student = get_object_or_404(Student, pk=student_id)
            selected_students.append(student)
        
        # Obtén las notas y consultas relacionadas con los estudiantes seleccionados
        gradesList = Grade.objects.filter(student__in=selected_students)
        consultaList = Consult.objects.filter(student__in=selected_students)
        bu = RegisNonAcademicActivity.objects.filter(student=student)
        expenses = Scholarship_expense.objects.filter(student = student )

        
        return render(request, 'generateReport.html', {
            "selected_students": selected_students,
            "grades": gradesList,
            "consultas": consultaList,
            "bu": bu,
            "expenses": expenses,
        })