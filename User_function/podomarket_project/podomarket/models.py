from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters
from django.core.validators import MinValueValidator


# Create your models here.

class User(AbstractUser):
    # AbstractUser 모델 생성
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        error_messages={'unique': '이미 사용중인 닉네임입니다.'},
        validators=[validate_no_special_characters],
    )
    kakao_id = models.CharField(
        max_length=20,
        null=True,
        validators=[validate_no_special_characters],
    )
    address = models.CharField(
        max_length=40,
        null=True,
        validators=[validate_no_special_characters],
    )

    def __str__(self):
        return self.email


class Post(models.Model):
    title = models.CharField(max_length=60)
    item_price = models.IntegerField(validators=[MinValueValidator(1)])

    status = [
        ("새제품", "새제품"),
        ("최상", "최상"),
        ("상", "상"),
        ("중", "중"),
        ("하", "하"),
    ]

    item_condition = models.CharField(choices=status, max_length=5, default=None)
    item_details = models.TextField(blank=True)
    image1 = models.ImageField(upload_to="item_pics")
    image2 = models.ImageField(blank=True, upload_to="item_pics")
    image3 = models.ImageField(blank=True, upload_to="item_pics")

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.title
