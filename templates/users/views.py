from django.shortcuts import render
import os

def login_view(request):
    print(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates/users/login.html'))
    return render(request, 'users/login.html')

