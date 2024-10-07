from django.shortcuts import render
from new_news.models import Play  # 모델 이름이 Play일 경우

def search_home(request):
    return render(request, 'search/search_home.html')

def search_results(request):
    query = request.GET.get('q')
    results = Play.objects.filter(title__icontains=query)  # 모델 이름에 맞게 수정
    return render(request, 'search/search_results.html', {'results': results, 'query': query})
