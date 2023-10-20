from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Book
from django.contrib import messages
# Create your views here.
def index(request):
    data = Book.objects.all()
    context = {"data" : data}
    return render(request,"index.html",context)

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        date=request.POST.get('date')
        provider=request.POST.get('provider')
        category=request.POST.get('category')
        print(name,desc,date,provider,category)
        query=Book(name=name,desc=desc,date=date,provider=provider,category=category)
        query.save()
        # Hien thi thong bao
        messages.info(request,"Dữ liệu sách đã được nhập vào")
    # return render(request,"index.html")
    return HttpResponseRedirect('/')

def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        desc=request.POST['desc']
        date=request.POST['date']
        provider=request.POST['provider']
        category=request.POST['category']

        edit = Book.objects.get(id=id)
        edit.name = name
        edit.desc = desc
        edit.date = date
        edit.provider = provider
        edit.category = category
        edit.save()

        messages.warning(request,"Dữ liệu sách đã được thay đổi")
        return redirect("/")

    d = Book.objects.get(id=id)
    context = {"d" : d}
    return render(request,"edit.html",context)
    # return HttpResponseRedirect('/')

def deleteData(request,id):
    d = Book.objects.get(id=id)
    d.delete()
    # context = {"data" : data}
    messages.error(request,"Dữ liệu sách đã được xóa")
    return redirect("/")
    # return HttpResponseRedirect('/')

def about(request):
    return render(request,"about.html")
