from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Создаем здесь представления. 
 
def barrack(request):
    return render(request,"barrack/barracks.html") 


