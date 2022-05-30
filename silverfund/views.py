from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from NewsSearch import NewsSearcher

ns = NewsSearcher()

def home(request):
    return render(request, 'silverfund/home.html')

def portfolio(request):
    return render(request, 'silverfund/portfolio.html')

def chatbot(request):
    if request.method == "POST":
        user_input = request.POST.get('user_query')
        bot_output = ns.get_answer(user_input)
        print(bot_output)
    return render(request, 'silverfund/chatbot.html')

def contacts(request):
    return render(request, 'silverfund/contacts.html')

