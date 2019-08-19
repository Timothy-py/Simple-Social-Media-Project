from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Accounts.forms import User_Reg

# Create your views here.

class User_Registration(CreateView):
    form_class = User_Reg
    success_url = reverse_lazy('login')
    template_name = 'Accounts/signup.html'
