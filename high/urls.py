from django.urls import path
from . import views

app_name='high'

urlpatterns = [
    path('',views.Down,name='Go'),
]
