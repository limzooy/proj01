from django.shortcuts import render

def new_news_list_view(request):
    # 새로운 뉴스 목록을 가져와서 템플릿으로 전달
    return render(request, 'news/new_news_list.html')