from django.shortcuts import render, redirect, get_object_or_404
from .models import Laboratorio
from .forms import LaboratorioForm

def lista_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio/lista.html', {'laboratorios': laboratorios})

def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_laboratorios')
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio/crear.html', {'form': form})

def editar_laboratorio(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('lista_laboratorios')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio/editar.html', {'form': form, 'laboratorio': laboratorio})


def eliminar_laboratorio(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('lista_laboratorios')
    return render(request, 'laboratorio/eliminar.html', {'laboratorio': laboratorio})
