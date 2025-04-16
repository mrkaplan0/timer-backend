from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializer import NoteSerializer

from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validation
        if not (username and email and password1 and password2):
            return render(request, 'timer/pages/registration_page.html', {'error_message': 'Alle Felder müssen ausgefüllt sein.'})
        
        if password1 != password2:
            return render(request, 'timer/pages/registration_page.html', {'error_message': 'Passwörter stimmen nicht überein.'})
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after successful registration
        except IntegrityError:
            return render(request, 'timer/pages/registration_page.html', 
                          {'error_message': 'Benutzername oder E-Mail existiert bereits.'})
    
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

def register_view(request):
    #register actions
    return render(request, 'timer/pages/registration_page.html')

def dashboard_view(request):
    # dashboard actions
    return render(request, 'timer/pages/dashboard.html')
