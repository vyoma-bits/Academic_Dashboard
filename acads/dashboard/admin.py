from django.contrib import admin
from .models import courses,grading,profs,tut2,Department,Branch,content1,marks,grade,student

admin.site.register(courses)
admin.site.register(Department)
admin.site.register(Branch)
admin.site.register(marks)
admin.site.register(content1)
admin.site.register(grade)
admin.site.register(student)
admin.site.register(grading)
admin.site.register(tut2)
admin.site.register(profs)






# Register your models here.
