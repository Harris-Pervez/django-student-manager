from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm



def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'add_student.html', {'form': form})


def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'update_student.html', {'form': form})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('home')

def poetic(request):
    return render(request,'shayri.html')

