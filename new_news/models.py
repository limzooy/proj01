from django.db import models

class Play(models.Model):  # 모델 이름이 Play일 경우
    title = models.CharField(max_length=200)
    # 기타 필드 추가
