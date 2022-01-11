from django import forms
from .models import User, Review


class SignupForm(forms.ModelForm):
    class Meta:  # 메타 클래스에 사용할 모델과 필드를 설정
        model = User
        fields = ["nickname"]

    def signup(self, request, user):
        user.nickname = self.cleaned_data["nickname"]  # form 에 기입된 데이터를 가져오기 위해 cleaned_data 사용
        user.save()


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "restaurant_name",
            "restaurant_link",
            "rating",
            "image1",
            "image2",
            "image3",
            "content",
        ]

        widgets = {
            "rating": forms.RadioSelect,
        }