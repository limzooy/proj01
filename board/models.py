from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
    
class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) #models.DO_NOTHING, db_column='author')
    created_date = models.DateField() #생성 날짜 및 시간을 포함하려면 DateTimeField를 사용하는 것이 좋음
    #created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'board'