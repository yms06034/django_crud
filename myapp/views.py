from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Name
from .forms import NameForm

from rest_framework import viewsets
from .serializers import NameSerializer

class NameViewSet(viewsets.ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSerializer



def name_list(request):
    names = Name.objects.all()
    return render(request, 'myapp/name_list.html', {'names': names})

def name_create(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('name_list')
    else:
        form = NameForm()
    return render(request, 'myapp/name_form.html', {'form': form})

def name_detail(request, id):
    name = get_object_or_404(Name, id=id)
    return render(request, 'myapp/name_detail.html', {'name': name})

def name_edit(request, id):
    name = get_object_or_404(Name, id=id)
    if request.method == 'POST':
        form = NameForm(request.POST, instance=name)
        if form.is_valid():
            form.save()
            return redirect('name_list')
    else:
        form = NameForm(instance=name)
    return render(request, 'myapp/name_form.html', {'form': form})

def name_delete(request, id):
    name = get_object_or_404(Name, id=id)
    if request.method == 'POST':
        name.delete()
        return redirect('name_list')
    return render(request, 'myapp/name_confirm_delete.html', {'name': name})


