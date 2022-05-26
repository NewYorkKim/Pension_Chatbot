from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'silverfund/home.html')

def portfolio(request):
    return render(request, 'silverfund/portfolio.html')

@csrf_exempt
def chatbot(request):
    return render(request, 'silverfund/chatbot.html')

def contacts(request):
    return render(request, 'silverfund/contacts.html')
