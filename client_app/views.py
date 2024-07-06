# client_app/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'client_app/index.html')
