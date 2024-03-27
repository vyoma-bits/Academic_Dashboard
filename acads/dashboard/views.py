


# Create your views here.=
from django.core.mail import send_mail
from django.http import FileResponse
from .models import courses,Department,profs,Branch,User,grading,content1,marks,grade,student,tut2
from django.forms import formset_factory
from .forms import courseForm,gradingForm,marksForm,contentForm,try1Form,tutForm
from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
import datetime
from datetime import datetime

def initial(request):
    return render(request,"dashboard/inital.html")

@staff_member_required(login_url='initial')
def courseform(request):
    submitted=False
    if request.method == "POST":
        form=courseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_course?submitted=True')
    else:
        form=courseForm
        if 'submitted' in request.GET:
            submitted=request.GET.get('submitted')
    return render(request,'dashboard/courseform.html',{'form':form,'submitted':submitted})
@staff_member_required(login_url='initial')
def display(request):

 

    return render(request,"dashboard/prof.html")
@staff_member_required(login_url='initial')
def tutform(request):
    dep1=[]

    dep=profs.objects.get(name=User.objects.get(username=request.user.username)).department
    dep1.append(dep.id)
    cou=courses.objects.all()
    courses1=[]
    for i in cou:
        if i.department == dep:
            courses1.append(i.id)

    submitted=False
    if request.method == "POST":
        form=tutForm(request.POST,courses=courses1,dep=dep1)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_course?submitted=True')
    else:
        form=tutForm(courses=courses1,dep=dep1)
        if 'submitted' in request.GET:
            submitted=request.GET.get('submitted')
    return render(request,'dashboard/courseform.html',{'form':form,'submitted':submitted})
@login_required
def display2(request):
   
    return render(request,"dashboard/index.html")



class MarksFormSet(formset_factory(marksForm, extra=0)):
    def __init__(self, *args, num_students, **kwargs):
        super().__init__(*args, **kwargs)
        if num_students:
            self.initial = [{} for _ in range(num_students)]  # Create initial forms

  # Create an empty formset for initial rendering
@login_required


def edit_profile(request):

    u=User.objects.get(username=request.user.username)
    try:
        department1=profs.objects.get(name=u).department.name
    except profs.DoesNotExist:
        department1=""
    if request.method == "POST":
          
          u.first_name=request.POST.get("f_name","")
          u.last_name=request.POST.get("l_name","")
          u.username=request.POST.get("bits_id","")
          u.age=request.POST.get("age","")
          u.user_mobile=request.POST.get("ph_number","")
          u.save()
          return redirect("display2")
    return render(request,"dashboard/edit_profile.html",{"data":u,"dept":department1})
@login_required
def add_to_tut(request):
    tut_id=request.session.get("tut_id")
    
    dep1=[]
    
   

    dep=profs.objects.get(name=User.objects.get(username=request.user.username)).department
    dep1.append(dep.id)
    tuts=tut2.objects.all()
    tut1=[]
    for i in tuts:
        if i.department == dep:
            tut1.append(i.name)
 
    cou=courses.objects.all()
    courses1=[]
    for i in cou:
        if i.department == dep:
            courses1.append(i.id)

    dep=profs.objects.get(name=User.objects.get(username=request.user.username)).department
    tut1=tut2.objects.get(name=tut_id,department=dep)
    form = tutForm(request.POST or None, instance=tut1,courses=courses1,dep=dep1,)
    if form.is_valid():
        form.save()
        # redirect to a new URL:
        return HttpResponse("succesful")
    return render(request, 'dashboard/add_to_tut.html', {'form': form})
def moderator(request):   # asking for tut section
    if request.method == "POST":
        u=request.POST.get("name","")
        request.session['tut_id']=u
        return redirect("tut2")
    return render(request,"dashboard/moderator.html")


    

    



def allcourses(request):
    selected_courses=[]

    user_id=request.user.username
    year=user_id[0:4]
    id1=user_id[4:6]
    ids = ['B1', 'B2', 'B3', 'B4', 'B5','A2','A7','A8','A4']   # FOR SOME BRANCHES ONLY
    branches = ['MSC BIO', 'MSC CHEM', 'MSC ECO', 'MSC MATHS', 'MSC PHYS','CIVIL','COMPUTER SCIENCE','ENI','MECHANICAL']
    id_branch_dict = dict(zip(ids, branches))
    years=['2023','2022','2021','2020','2019']
    ids1=[1,2,3,4,5]
    id_year_dict = dict(zip(years, ids1))

    user_branch=id_branch_dict[id1]
    user_year=id_year_dict[year]
    course_year=int(str(user_year)+"2") # year and taking 2nd sem



 
        #for now it is only avaliable for singlities and for dualities their msc degree
  
    u=courses.objects.all()
    electives=[]
    cdc=[]
    try:
        su=student.objects.get(name=User.objects.get(username=request.user.username))
    except student.DoesNotExist:
        

        su=student(name=User.objects.get(username=request.user.username),branch=Branch.objects.get(name=user_branch))
        su.save()
    for i in u:
        
        if i.cdc == True and Branch.objects.get(name=user_branch) in i.branches.all() and i.year == course_year:
            cdc.append(i)
            su=student.objects.get(name=User.objects.get(username=request.user.username))
            su.opted_courses.add(i)
            su.save()
            


        else:
            if  Branch.objects.get(name=user_branch) in i.branches.all() and i.year == course_year:
                electives.append(i)
        io2=student.objects.get(name=User.objects.get(username=request.user.username))
        sel=io2.opted_courses.all()


     
    return render(request,"dashboard/allcourses.html",{"electives":electives,"cdc":cdc,"all":sel})

def login1(request):
    return render(request,'dashboard/google_login.html')
@staff_member_required(login_url='initial')
def grading1(request):
    submitted=False
    if request.method == "POST":
        form=gradingForm|(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('dashboard/form_result?submitted=True')
    else:
        form=gradingForm
        if 'submitted' in request.GET:
            submitted=request.GET.get('submitted')
    return render(request,'dashboard/gradingform.html',{'form':form,'submitted':submitted})
@staff_member_required(login_url='initial')
def marksform(request):
    submitted=False
    if request.method == "POST":
        form=marksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('dashboard/form_result?submitted=True')
    else:
        form=marksForm
        if 'submitted' in request.GET:
            submitted=request.GET.get('submitted')
    return render(request,'dashboard/marksform.html',{'form':form,'submitted':submitted})
@staff_member_required(login_url='initial')
def add_content(request):
    submitted=False
    course1=[]
    cou=courses.objects.all()
    for i in cou:
            if i.department == profs.objects.get(name=User.objects.get(username=request.user.username)).department:
                course1.append(i.id)
    print(course1)
    
    if request.method == "POST":
        student1 = User.objects.get(username=request.user.username)
        form=contentForm(request.POST,request.FILES,initial={'user': student1},courses=course1)
        if form.is_valid():
            form.save()
            course = form.cleaned_data.get('course')
            users_email=[]
            users=student.objects.all()
            for i in users:
                if course in i.opted_courses.all():
                    users_email.append(i.name.email)
            for i in users_email:
                send_mail(
        subject="New announcement for your course ",
        message="plz log in the dashboard to see",
        from_email=None, # use DEFAULT_FROM_EMAIL if None
        recipient_list=[i],)
       
            
           

            return HttpResponseRedirect('add_content?submitted=True')
    else:
        student1 = User.objects.get(username=request.user.username)
        form=contentForm(initial={'user': student1},courses=course1)
        if 'submitted' in request.GET:
            submitted=request.GET.get('submitted')
    return render(request,'dashboard/contentform.html',{'form':form,'submitted':submitted})
@staff_member_required(login_url='initial')
def evaluations(request):
    dep_prof=profs.objects.get(name=User.objects.get(username=request.user.username)).department.name
    courses_under_department=[]
    ui=courses.objects.all()
    for i in ui:
        if i.department.name == dep_prof:
            courses_under_department.append(i)
  
    
    

    
    stu_dep=[]
    submitted=True
    st=student.objects.all()
    for i in st:
        opted=i.opted_courses.all()
        print(opted)
    
        if any(element in opted for element in courses_under_department) :
            stu_dep.append(i.name)
    
 
    
    
    
    return render(request,'dashboard/dep_students.html',{'submitted':submitted,'students':stu_dep})
def add_tut(request):
    submitted=False
    dep=profs.objects.get(name=User.objects.get(username=request.user.username)).department
    courses1=[]
    yt=courses.objects.all()
    teachers=[]
    te=profs.objects.all()
    dep1=[]
    dep1.append(dep.id)
    for i in te:
        if i.department == dep:
            teachers.append(i.id)
    for i in yt:
        if i.department == dep :
            courses1.append(i.id)
    
        
    if request.method == "POST":
       
        form=tutForm(request.POST,dep=dep1,courses=courses1,teac=teachers)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_content?submitted=True')
    else:
        
        form=tutForm(dep=dep1,courses=courses1,teac=teachers)
        if 'submitted' in request.GET:
            submitted=request.GET.get('submitted')
    return render(request,'dashboard/contentform.html',{'form':form,'submitted':submitted})

@staff_member_required(login_url='initial')

def marks2(request,profile_id):
    dep=profs.objects.get(name=User.objects.get(username=request.user.username)).department
    courses_dep=[]
    cop=courses.objects.all()
    for i in cop:
        if i.department == dep:
            courses_dep.append(i)
    courses_student=[]
    student1 = User.objects.get(username=profile_id)
    st_courses=student.objects.get(name=student1).opted_courses.all()
    common_elements = [element for element in st_courses if element in courses_dep]
    for i in common_elements:
        courses_student.append(i.id)
    

    
    
    

    
    
   
    if request.method == 'POST':

        student1 = User.objects.get(username=profile_id)
        course1=courses.objects.all()

        marks_form = marksForm(request.POST,initial={'user': student1},courses=courses_student)
        if marks_form.is_valid():
            marks_form.save()
            return redirect('evaluation')
            
   
    else:
       
        student1 = User.objects.get(username=profile_id)
        marks_form = marksForm(initial={'user': student1},courses=courses_student)
    
    return render(request,'dashboard/evaluationform.html',{'marks_forms': marks_form,'submitted':False})
@staff_member_required(login_url='initial')

def courses1(request):
    prof_dept=profs.objects.get(name=User.objects.get(username=request.user.username)).department
    courses1=[]
    co=courses.objects.all()
    for i in co:
       
        
            if i.department == prof_dept:
                courses1.append(i)
                
        
    return render(request,"dashboard/allgrades.html",{"courses":courses1})
@staff_member_required(login_url='initial')

def add_grading(request,profile_id):
   
    
   
    if request.method == 'POST':
        course = courses.objects.get(course_name=profile_id)
        marks_form = gradingForm(request.POST,initial={'course': course})
        if marks_form.is_valid():
            marks_form.save()
            ga = marks_form.cleaned_data.get('ga')
            g_a = marks_form.cleaned_data.get('g_a')
            gb = marks_form.cleaned_data.get('gb')
            g_b = marks_form.cleaned_data.get('g_b')
            g_c = marks_form.cleaned_data.get('g_c')
            gc = marks_form.cleaned_data.get('gc')
            gd = marks_form.cleaned_data.get('gd')
            course=marks_form.cleaned_data.get('course')
            students=[]
            ui=student.objects.all()
            for i in ui:
                if course in i.opted_courses.all():
                    students.append(i)
            for j in students:
                io=marks.objects.get(user=j.name)
                total_marks=io.mid_sem+io.compre+io.evals
                grade_boundaries = {
    'A': ga,
    'A-': g_a,
    'B': gb,
    'B-': g_b,
    'C': g_c,
    'C-': gc,
    'D': gd
}
                assigned_grade = next((grade for grade, boundary in sorted(grade_boundaries.items(), key=lambda x: x[1], reverse=True) if total_marks >= boundary), 'NC')
                grade_s=grade(name=j.name,course=course,grade=assigned_grade)
                grade_s.save()



            

            

            
        
            
            return redirect('evaluation')
            
   
    else:
        course = courses.objects.get(course_name=profile_id)
        marks_form = gradingForm(initial={'course': course})
    
    return render(request,'dashboard/gradingform.html',{'form': marks_form,'submitted':False})
@login_required

def announcements(request):
    ann=content1.objects.all()
    user=User.objects.get(username=request.user.username)
    try:
        courses1=student.objects.get(name=user).opted_courses.all()
    except student.DoesNotExist:
        return HttpResponse("YOU HAVE NOT BEEN ENROLLED IN ANY COURSE PLZ DO")
    ann1=[]
    for i in ann:
        for j in courses1:
            if j == i.course:
                ann1.append(i)


    return render(request,"dashboard/announcements.html",{"announcements":ann1})
@login_required

def download(request,pk):
    announcement = content1.objects.get(pk=pk)
    file = announcement.file
    filename = file.name
    response = FileResponse(file, as_attachment=True)
    response['content1-Disposition'] = 'attachment; filename='+filename
    return response
@staff_member_required(login_url='initial')
def try1(request):
    prof_dept=profs.objects.get(name=User.objects.get(username=request.user.username)).department
    courses1=[]
    co=courses.objects.all()
    for i in co:
       
        
            if i.department == prof_dept:
                courses1.append(i.id)
                
    submitted=False
    if request.method == "POST":
        form=try1Form(request.POST,courses=courses1)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            course = form.cleaned_data.get('course')
            try:
                student2=student.objects.get(name=name)
                student2.opted_courses.add(course)
            except student.DoesNotExist:
                student21=student(name=name,branch=Branch.objects.get(name="MSC BIO"))
                student21.save()
                student21=student.objects.get(name=name)
                student21.opted_courses.add(course)
                student21.save()
                

            
            
            return HttpResponseRedirect('try1?submitted=True')
    else:
        form=try1Form(courses=courses1)
        if 'submitted' in request.GET:
            submitted=request.GET.get('submitted')
    return render(request,'dashboard/try1form.html',{'form':form,'submitted':submitted})
@login_required

def add_cart(request,pk):
    
    stu=student.objects.get(name=User.objects.get(username=request.user.username))
  
    if courses.objects.get(pk=pk) in stu.opted_courses.all():
        return HttpResponse("already added")
    else:
        stu.opted_courses.add(courses.objects.get(pk=pk))
        stu.save()
        return redirect("allcourses")
@login_required

def see_grades(request):
    cgpa=0
    units=0
    score=0
    ui=grade.objects.all()
    courses13=[]
    for i in ui:
        if i.name == User.objects.get(username=request.user.username) :
            courses13.append(i)
            units=units+i.course.credits
            grade1 = i.grade.upper()
            mapping = {'A': 10, 'A-': 9, 'B': 8, 'B-': 7, 'C': 6, 'D': 5,'NC':0}
            score=score+mapping.get(grade1, None)
    cgpa=score/units
    
    
    return render(request,"dashboard/see_grades.html",{"grades":courses13,"cgpa":cgpa})
def loginf(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)

        if user is not None:

            login(request,user)

            # Pass the username to the redirected view using a context variable

            return redirect("display")





        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'dashboard/loginc.html')






   
      
  



        













