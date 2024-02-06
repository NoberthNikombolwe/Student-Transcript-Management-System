from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Department)
admin.site.register(Staff)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Class)

admin.site.register(Student)
admin.site.register(Result)
admin.site.register(HeadOfDepartment)
admin.site.register(TeacherAssignment)
admin.site.register(ClassModule)
admin.site.register(Semester)



