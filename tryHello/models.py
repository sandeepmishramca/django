from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    # if you want to give your own PK 
    student_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True) #every time it will create 

class Course(models.Model):
    name = models.CharField(max_length=100)
    # if you want to use TextField for large text then no need to specify max_length
    description = models.TextField()
    # student : course  M:M

class Enrolment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrol_date = models.DateTimeField(auto_now_add=True)

# create own table name then use meta sub class inside model class
class TestTable(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        db_table = 'abc_table'
        ordering = ['name'] # user -name for desencding ording