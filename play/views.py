from django.shortcuts import render

def play_list_view(request):
    # 연극 목록을 가져와서 템플릿으로 전달
    return render(request, 'play/play_list.html') 
