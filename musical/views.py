from django.shortcuts import render

def musical_list_view(request):
    # 공연 목록을 가져와서 템플릿으로 전달
    return render(request, 'musical/musical_list.html')  # 해당 템플릿 파일의 경로 확인
