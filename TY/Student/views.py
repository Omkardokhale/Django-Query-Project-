from django.shortcuts import render
from django.http import HttpResponse
from Student.models import Blog, Author, Entry
# Create your views here.



def view_base(request):
     
    stud_base = Author.objects.all()
    return render(request,'base.html',{'stud1':stud_base})

def view_base1(request):
     
    stud_base1 = Entry.objects.all()
    return render(request,'base1.html',{'stud2':stud_base1})

def view_base2(request):
     
    stud_base2 = Blog.objects.all()
    return render(request,'base2.html',{'stud3':stud_base2})
