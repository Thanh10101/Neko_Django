from django.shortcuts import render
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