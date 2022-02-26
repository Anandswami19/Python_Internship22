from multiprocessing import context
from urllib import request
from django.shortcuts import render
from .models import Student


def studentData(request):
    students=Student.objects.all().values()
    students1=Student.objects.filter(student_name__startswith='D').values()
    students2=Student.objects.filter(student_name__contains='t').values()
    print('filter',students1)
    print('filter',students2)
    print(students[0].get('id'))
    print(students[0])
    studentlist=[]
    for i in students1[0].values():
        studentlist.append(i)

    print('studentlist =',studentlist)


    context={
        'students':studentlist
    }

    return render(request,'orm/student.html',context)
    students = Student.objects.all().values()
    
    

