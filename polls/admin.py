from django.contrib import admin

# Register your models here.
#admin 관련하여 등록하고 싶은 것을 여기에 작성
from .models import Question
admin.site.register(Question)