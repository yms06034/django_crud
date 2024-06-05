from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Name
from .forms import NameForm

from rest_framework import viewsets
from .serializers import NameSerializer

class NameViewSet(viewsets.ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSerializer


