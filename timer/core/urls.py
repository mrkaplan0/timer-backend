# myapp/urls.py

from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='landing_page'),
    path('login/', views.login_view, name='login_page'),
    path('register/', views.register_view, name='register_page'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='landing_page'), name='logout'),
]
