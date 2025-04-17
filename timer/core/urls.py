# myapp/urls.py

from django.urls import path
from . import views  
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Existierende URLs
    path('', views.index, name='landing_page'),
    path('register/', views.register_view, name='register_page'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='landing_page'), name='logout'),

    # Login-URLs hinzufügen
    path('login/', views.login_view, name='login'),
    path('login-page/', views.login_view, name='login_page'),  # Alias für dieselbe View

    # APIs
    path('api/notes/', views.note_list_create, name='note-list-create'),
]
