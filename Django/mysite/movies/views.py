from django.shortcuts import render
from rest_framework import viewsets
from movies.models import Moviedata
from movies.serializers import MoviedataSerializer

# Create your views here.
class MoviedataViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MoviedataSerializer

class ActionMoviesViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='action')
    serializer_class = MoviedataSerializer

class ComedyMoviesViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='comedy')
    serializer_class = MoviedataSerializer