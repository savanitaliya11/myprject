from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')


def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        tel = request.POST.get('contact')
        email = request.POST.get('email')
        drop = request.POST.get('select')
        mes = request.POST.get('message')
        result = Students(name=name, contact=tel, email=email, select=drop, message=mes)
        result.save()
        return redirect('show')


def show(request):
    result = Students.objects.all()
    params = {
        'result': result
    }
    return render(request, 'show.html', params)


def delete(request, id):
    instance = Students.objects.get(id=id)
    instance.delete()
    return redirect('show')


def update(request, id):
    result = Students.objects.get(id=id)
    params = {
        'result': result
    }
    return render(request, 'update.html', params)


def edit(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        tel = request.POST.get('contact')
        email = request.POST.get('email')
        drop = request.POST.get('select')
        mes = request.POST.get('message')

        if id != 0:
            Students.objects.filter(id=id).update(name=name, contact=tel, email=email, select=drop, message=mes)
            return redirect('show')
    else:
        return render(request, 'show.html')
