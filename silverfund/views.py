from cv2 import add
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
import pandas as pd
import json

from FundRanks import FundRanker
from NewsSearch import NewsSearcher
from QnA import Chatbot

ns = NewsSearcher()
ch = Chatbot()
fr = FundRanker()

def home(request):
    return render(request, 'silverfund/home.html')

def portfolio(request):
    return render(request, 'silverfund/portfolio.html')

def chatbot(request):
    return render(request, 'silverfund/chatbot.html')

def ranks(request):
    data = json.loads(request.body)
    score = data.get('score')
    result1 = data.get('result1')
    result2 = data.get('result2')

    show_result1(request, result1), show_result2(request, result2)
    
    # (result1, result2) = fr.data_call(score)
    # result = pd.read_excel('result/result1_sample_3.xlsx', usecols="D:R")

    context = {
        "score": score,
        "result1": "porfolio/result1/",
        "result2": "portfolio/result2/"
    }

    return JsonResponse(context)

def show_result1(request, file=None):
    if file is None:
        address = 'silverfund/home.html'
    else:
        address = f'silverfund/result/{file}.html'
    return render(request, address)

def show_result2(request, file=None):
    if file is None:
        address = 'silverfund/home.html'
    else:
        address = f'silverfund/result/{file}.html'
    return render(request, address)

def qna(request):
    question = json.loads(request.body)
    user_input = question.get('text')

    bot_output = ch.get_answer(user_input)

    context = {"text": bot_output,
               "user": False,
               "chatbot": True}

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

