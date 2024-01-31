from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


def cars_list(request):
    cars = Car.objects.all()
    return render(request, 'cars_list.html', {'cars': cars})


def cars_detail(request, pk):
    cars = get_object_or_404(Car, pk=pk)
    comments = Comment.objects.filter(cars_text=cars)
    car_photos = CarPhoto.objects.filter(cars_photo=cars)
    return render(request, 'cars_detail.html', {'cars': cars, 'comments': comments, 'car_photos': car_photos})


def cars_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            cars = form.save()
            return redirect('cars_detail', pk=cars.pk)
    else:
        form = CarForm()
    return render(request, 'cars_create.html', {'form':form})


def cars_update(request, pk):
    cars = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=cars)
        if form.is_valid():
            cars = form.save()
            return redirect('cars_detail', pk=cars.pk)
    else:
        form = CarForm(instance=cars)
    return render(request, 'cars_update.html', {'form':form, 'cars': cars})


def cars_delete(request, pk):
    cars = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        cars.delete()
        return redirect('cars_list')
    return render(request, 'cars_delete.html', {'cars': cars})
