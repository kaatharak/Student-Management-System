from django.shortcuts import render, redirect

from Student.models import Student


# Create your views here.
def home(request):
    return render(request,'home.html')


def display_fun(request):
    students = Student.objects.all()
    data = {'students' : students}
    return render(request,'displaystudent.html',data)


def add_fun(request):
    if request.method == 'GET':
        return render(request,'addstudent.html')
    else:
        student = Student()
        student.Name = request.POST['tbname']
        student.Age = request.POST['tbage']
        student.City = request.POST['tbcity']
        student.Email = request.POST['tbemail']
        student.Phone = request.POST['tbphone']
        student.save()
        return redirect('displaystudents')




def edit_fun(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'GET':
        data = {"student":student}
        return render(request,'editstudent.html',data)
    else:
        student.Name = request.POST['tbname']
        student.Age = request.POST['tbage']
        student.City = request.POST['tbcity']
        student.Email = request.POST['tbemail']
        student.Phone = request.POST['tbphone']
        student.save()
        return redirect('displaystudents')


def delete_fun(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('displaystudents')
