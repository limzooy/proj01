from django.shortcuts import render
from .models import ExhibitionEvent

def exhibition_event_list_view(request):
    # 혜택 목록을 가져와서 템플릿으로 전달
    return render(request, 'exhibition_event/exhibition_event_list.html')  # 해당 템플릿 파일의 경로 확인

def post_view(request):
    posts = Post.objects.all() #Post테이블의 모든 객체 불러와서 posts변수에 저장
    return render(request, 'index.html',{"posts": posts})