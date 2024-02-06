# models.py

from django.db import models

class Semester(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Staff(models.Model):
    EDE_level = (
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('PhD', 'PhD'),
        ('Profesor', 'Prof')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    education_level = models.CharField(max_length=50, choices=EDE_level)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class HeadOfDepartment(models.Model):
    department = models.OneToOneField(Department, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return f"Head of {self.department} - {self.staff}"

class Course(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Module(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    credit = models.CharField(max_length=150, default="6")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Class(models.Model):
    time_ = (
        ('Full-time', 'Full-time'),
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),  
    )
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time = models.CharField(max_length=20, choices=time_)  # 'afternoon' or 'night'

    def __str__(self):
        return self.name
    
class ClassModule(models.Model):
    class_module = models.ForeignKey(Class, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.class_module} - {self.module} - {self.semester}"

    
class TeacherAssignment(models.Model):
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher} - {self.module}"

class Student(models.Model):
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=15, choices=GENDER)
    registration_number = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Result(models.Model):
    semester_dur = (
        ('1', '1'),
        ('2', '2'),
    )
    year_dur = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    year = models.CharField(max_length=1, choices=year_dur)  # 1, 2, 3, or 4
    ca = models.FloatField()
    fe = models.FloatField()

    def calculate_grade(self):
        total_marks = self.ca + self.fe

        if total_marks >= 70:
            return 'A'
        elif 60 <= total_marks < 70:
            return 'B+'
        elif 50 <= total_marks < 60:
            return 'B'
        elif 40 <= total_marks < 50:
            return 'C'
        elif 30 <= total_marks < 40:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        return f"{self.student} - {self.module} - Semester {self.semester}, Year {self.year}"

