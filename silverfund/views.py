from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from pydantic import Json
from NewsSearch import NewsSearcher
from QnA import Chatbot

ns = NewsSearcher()
ch = Chatbot()

def home(request):

    return render(request, 'silverfund/home.html')

def portfolio(request):
    return render(request, 'silverfund/portfolio.html')

def chatbot(request):
    return render(request, 'silverfund/chatbot.html')

def qna(request):
    question = json.loads(request.body)
    user_input = question.get('text')

    bot_output = ch.get_answer(user_input)

    context = {"text": bot_output,
               "user": False,
               "chatbot": True
    }

    return JsonResponse(context)

def news(request):
    question = json.loads(request.body)
    user_input = question.get('text')

    bot_output = ns.get_answer(user_input)

    context = {"text": bot_output,
               "user": False,
               "chatbot": True}
     
    return JsonResponse(context)

def contacts(request):
    return render(request, 'silverfund/contacts.html')

