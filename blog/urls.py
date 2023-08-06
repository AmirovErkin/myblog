from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('password/<str:complexity>', views.generate_password, name='generate-password'),
]
