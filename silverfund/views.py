from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from pydantic import Json
from NewsSearch import NewsSearcher

ns = NewsSearcher()

def home(request):

    return render(request, 'silverfund/home.html')

def portfolio(request):
    return render(request, 'silverfund/portfolio.html')

def chatbot(request):
    #     return JsonResponse(question)
    #     user_input = request.POST.get('user_query')
    #     bot_output = ns.get_answer(user_input)
    #     context = json.dumps(bot_output)
    #     return render(request, 'silverfund/chatbot.html', context)
    # else:
    return render(request, 'silverfund/chatbot.html')

def send(request):
    question = json.loads(request.body)
    user_input = question.get('text')

    bot_output = '입력: ' + user_input

    context = {'text': bot_output}
     
    return JsonResponse(context)

def contacts(request):
    return render(request, 'silverfund/contacts.html')

