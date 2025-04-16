from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializer import NoteSerializer

#registrations view
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validation pw
        if not (username and email and password1 and password2):
            messages.error(request, 'Alle Felder müssen ausgefüllt sein.')
            return render(request, 'timer/pages/registration_page.html')
        
        if password1 != password2:
            messages.error(request, 'Passwörter stimmen nicht überein.')
            return render(request, 'timer/pages/registration_page.html')
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)  # login user after registration
            messages.success(request, 'Registrierung erfolgreich!')
            return redirect('dashboard')  # direct to dashboard after registration
        except IntegrityError:
            messages.error(request, 'Benutzername oder E-Mail existiert bereits.')
            return render(request, 'timer/pages/registration_page.html')
    
    return render(request, 'timer/pages/registration_page.html')

@api_view(['GET', 'POST'])
def note_list_create(request):
    if request.method == 'GET':
        notes = Note.objects.all()       
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


def index(request):
    return render(request, 'timer/pages/landing_page.html')

def login_view(request):
    #login actions
    return render(request, 'timer/pages/login_page.html')

@login_required(login_url='login_page')  # Giriş yapmamış kullanıcıları login sayfasına yönlendirir /leitet nicht Angemeldete nutzer automatisch weiter zur Anmeldeseite
def dashboard_view(request):
    return render(request, 'timer/pages/dashboard.html')
