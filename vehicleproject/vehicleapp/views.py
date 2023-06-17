from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Vehicle
from . forms import VehicleForm

# Create your views here.

def index(request):
    vehicle=Vehicle.objects.all()
    context={
        'vehicle_list':vehicle
    }
    return render(request, 'index.html',context)

def detail(request,vehicle_id):
    vehicle=Vehicle.objects.get(id=vehicle_id)
    return render(request,"detail.html",{'vehicle':vehicle})

def add_vehicle(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        vehicle=Vehicle(name=name, desc=desc, year=year, img=img)
        vehicle.save()

    return render(request,'add.html')

def update(request,id):
    vehicle=Vehicle.objects.get(id=id)
    form=VehicleForm(request.POST or None, request.FILES, instance=vehicle)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'edit.html', {'form':form, 'vehicle':vehicle})

def delete(request, id):
    if request.method=='POST':
        vehicle=Vehicle.objects.get(id=id)
        vehicle.delete()
        return redirect('/')

    return render(request, 'delete.html')


