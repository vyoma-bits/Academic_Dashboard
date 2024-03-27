from django.db import models
from django.contrib.auth.models import User
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Branch(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class courses(models.Model):
    course_name=models.CharField(max_length=250)
    cdc=models.BooleanField()
    elective=models.BooleanField()
    credits=models.IntegerField()
    year=models.IntegerField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.course_name
    branches = models.ManyToManyField(Branch)

class profs(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'is_staff': True})
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    courses_undertaken=models.ManyToManyField(courses)
    def __str__(self):
        return self.name.username

class student(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'is_staff': False})
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    opted_courses=models.ManyToManyField(courses)
class tut2(models.Model):
    name=models.CharField(max_length=50)
    course=models.ForeignKey(courses,on_delete=models.CASCADE)
    students=models.ManyToManyField(User,limit_choices_to={'is_staff': False})
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    teacher=models.ForeignKey(profs,on_delete=models.CASCADE)




  ## 21 or 12
class grading(models.Model):
    course=models.ForeignKey(courses,on_delete=models.CASCADE)
    ga=models.IntegerField()
    g_a=models.IntegerField()
    gb=models.IntegerField()
    g_b=models.IntegerField()
    gc=models.IntegerField()
    g_c=models.IntegerField()
    gd=models.IntegerField()
class content1(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.FileField(upload_to='uploads/', max_length=254,blank=True)
    description=models.CharField(max_length=269)
    course=models.ForeignKey(courses,on_delete=models.CASCADE)
class marks(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(courses,on_delete=models.CASCADE)
    mid_sem=models.IntegerField()
    evals=models.IntegerField()
    compre=models.IntegerField()
class grade(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(courses,on_delete=models.CASCADE)
    grade=models.CharField(max_length=2)
class try1(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'is_staff': False})
    course=models.ForeignKey(courses,on_delete=models.CASCADE)














# Create your models here.
