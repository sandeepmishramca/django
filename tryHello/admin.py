from django.contrib import admin
from tryHello.models import Student, Course, Enrolment
# Register your models here.Django admin provide a UI , from where can be edit and show , filter over the UI

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrolment)

# create a custom admin penal , Django penal provide a history of the table update
class StudentAdmin(admin.ModelAdmin):
    list_filter = (('name'),)
    list_display = ('name','age')
    list_editable = (('name','age'))

admin.register(Student,StudentAdmin)

