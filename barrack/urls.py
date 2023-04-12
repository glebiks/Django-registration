from django.urls import path
from . import views

urlpatterns = [
    path('', views.barrack, name="barrack"),
]