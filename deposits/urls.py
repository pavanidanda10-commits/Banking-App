from .views import deposits
from django.urls import path

urlpatterns = [
    path('', deposits, name='deposits'),
]