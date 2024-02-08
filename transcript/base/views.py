# views.py

from django.shortcuts import render, get_object_or_404
from .models import Student, Result
from django.contrib.auth.decorators import login_required

def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'student_list.html', context)

def transcript_view(request, student_id):
    student = Student.objects.get(pk=student_id)
    results = Result.objects.filter(student=student)

    # Calculate GPA for each semester
    semesters = {}
    total_grade_points = 0
    total_credits = 0

    for result in results:
        semester_key = f"Semester {result.semester} - Year {result.year}"
        if semester_key not in semesters:
            semesters[semester_key] = {
                'results': [],
                'gpa': 0
            }
        semesters[semester_key]['results'].append(result)

        # Calculate GPA for the current result and add it to the total
        grade_points = get_grade_points(result.calculate_grade())
        total_grade_points += grade_points
        # Here we're counting each module equally weighted, assuming no 'credit' attribute
        total_credits += 1

    # Calculate GPA for each semester
    for semester_data in semesters.values():
        results = semester_data['results']
        semester_gpa = sum([get_grade_points(result.calculate_grade()) for result in results]) / len(results)
        semester_data['gpa'] = semester_gpa

    # Calculate overall GPA
    overall_gpa = total_grade_points / total_credits

    context = {
        'student': student,
        'semesters': semesters,
        'overall_gpa': overall_gpa,
    }
    return render(request, 'transcript.html', context)



def get_grade_points(grade):
    if grade == 'A':
        return 5
    elif grade == 'B+':
        return 4
    elif grade == 'B':
        return 3
    elif grade == 'C':
        return 2
    elif grade == 'D':
        return 1
    else:
        return 0
