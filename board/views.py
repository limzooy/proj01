from django.shortcuts import render

def board_list_view(request):
    # 게시판 목록을 가져와서 템플릿으로 전달
    return render(request, 'board/board_list.html')