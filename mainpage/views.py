from django.shortcuts import render

def mainpage_home(request):
    return render(request, 'mainpage/mainpage.html')