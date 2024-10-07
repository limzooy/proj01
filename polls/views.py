from django.shortcuts import render

# Create your views here.
# 응답 데이터를 만들어줌. HttpResponse
# view의 기능 = 요청을 처리하는 핵심 기능
from django.http import HttpResponse
from django.views.generic import View

def index(request):
    print('클라이언트의 요청을 받음')
    print('요청을 처리(완료하려면 엔터)')
    return HttpResponse("""
                        <!DOCTYPE html>
                        <html>
                            <head>
                                <title>Index</title>
                            </head>
                            <body>
                            <h1>하이!</h1>
                            </body>
                        </html>
                        """)

def mainpage(request):
    return render(request, "mainpage.html")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're votion on question %s." % question_id)