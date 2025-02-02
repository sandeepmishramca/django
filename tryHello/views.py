from django.shortcuts import render
from django.http import HttpResponse
import datatime
from tryHello.models import Student

# Create your views here.
# def hello_world(request, name):
#     msg = f'Hello {name}'
#     return HttpResponse(msg)

# def hello_world(request, name):
#     s1 = Student(name='sandeep', age=10, dob=datatime.date.today())
#     s1.save() # to Store the date in DB, it will save in DB
#     msg = f'Hello {name}'
#     return HttpResponse(msg)

# def hello_world(request, name):
#     # all_student = Student.objects.all() # to fect all records from student
#     student = Student.objects.get(name=name) # to get student by name
#     msg = f'Hello Your age is {str(student.age)}'
#     return HttpResponse(msg)

def hello_world(request, name):
    # update the age and save to DB
    student = Student.objects.get(name=name) # to get student by name
    student.age=15
    student.save()
    msg = f'Hello Your age is {str(student.age)}'
    return HttpResponse(msg)
