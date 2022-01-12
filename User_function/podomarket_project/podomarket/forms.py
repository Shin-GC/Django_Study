from django import forms
from .models import User, Post


class SignupForm(forms.ModelForm):  # 회원가입시 추가 폼
    class Meta:
        model = User
        fields = ["nickname", "kakao_id", "address"]  # 추가 입력 받을 필드

    def signup(self, request, user):
        user.nickname = self.cleaned_data["nickname"]  # Form 에 기입된 데이터를 가져오기 위해 cleaned_data 사용
        user.kakao_id = self.cleaned_data["kakao_id"]
        user.address = self.cleaned_data["address"]
        user.save() # 꼭 저장해주기


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "item_price",
            "item_condition",
            "item_details",
            "image1",
            "image2",
            "image3",
        ]

        widgets = {
            "item_condition": forms.RadioSelect,
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "item_price",
            "item_condition",
            "item_details",
            "image1",
            "image2",
            "image3",
            "is_sold",
        ]
        widgets = {
            "item_condition": forms.RadioSelect,
        }