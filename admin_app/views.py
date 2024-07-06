# admin_app/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'admin_app/index.html')
