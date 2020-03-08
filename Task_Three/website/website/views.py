from django.shortcuts import render, redirect
from django.contrib import messages

# register view
def home(request):
    # reg = Registration()
    print(request.method)
    return render(request, 'index.html')
