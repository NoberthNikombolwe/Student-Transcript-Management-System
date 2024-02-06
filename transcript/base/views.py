# views.py

from django.shortcuts import render, get_object_or_404
from .models import Student, Result

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
# views.py

from django.shortcuts import render
from .models import Student, Result

def transcript_view(request, student_id):
    student = Student.objects.get(pk=student_id)
    results = Result.objects.filter(student=student)

    # Calculate GPA for each semester
    semesters = {}
    for result in results:
        semester_key = f"Semester {result.semester} - Year {result.year}"
        if semester_key not in semesters:
            semesters[semester_key] = []
        semesters[semester_key].append(result)

    for semester_key, results in semesters.items():
        total_grade_points = 0
        total_credits = 0
        for result in results:
            grade_points = get_grade_points(result.calculate_grade())
            total_grade_points += grade_points
            # Here we're counting each module equally weighted, assuming no 'credit' attribute
            total_credits += 1
        semester_gpa = total_grade_points / len(results)
        semesters[semester_key] = {
            'results': results,
            'gpa': semester_gpa,
        }

    # Calculate overall GPA
    total_grade_points = sum([get_grade_points(result.calculate_grade()) for result in results])
    total_credits = len(results)  # Using the number of results for overall GPA calculation
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
