from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def client(request):
    return render(request, 'client/client.html');
