from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, 'silverfund/home.html')

def portfolio(request):
    return render(request, 'silverfund/portfolio.html')

def chatbot(request):
    return render(request, 'silverfund/chatbot.html')

def contacts(request):
    return render(request, 'silverfund/contacts.html')
