from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView,View, CreateView
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):        
    return render(request , 'official/home.html')
