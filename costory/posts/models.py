from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50, unique=True, error_messages={'unique': '이미 동일한 제목으로 쓴 글이 있습니다.'})
    content = models.TextField()
    #  Char 와 Text 필드의 차이는 Char 는 길이제한을 설정하지만 Text 는 길이제한이 없다!
    dt_created = models.DateTimeField(verbose_name='Date Created', auto_now_add=True)
    #  DateTimefield 는 날짜와 시간을 함께 담을 수 있는 필드
    #  verbose_name 은 사람이 읽기 좋은 필드명을 지정해주는 인자로 나중에 이 필드를 볼때 알아보기 편하라고 별명을 붙여주는 것!
    dt_modified = models.DateTimeField(verbose_name='Date Modified', auto_now=True)

    def __str__(self):
        return self.title
    # Post 객체를 하나의 문자열로 표현하기 위해 작성
