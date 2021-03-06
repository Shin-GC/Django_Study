from django.contrib import admin
from .models import User, Post
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(User, UserAdmin)  # admin에 모델 등록
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname", "kakao_id", "address")}),)

admin.site.register(Post)