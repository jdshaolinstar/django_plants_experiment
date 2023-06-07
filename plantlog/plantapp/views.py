from django.shortcuts import render, redirect
from .forms import PlantForm
from .models import Plant

def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'plantapp/plant_list.html', {'plants': plants})

def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm()
    return render(request, 'plantapp/add_plant.html', {'form': form})