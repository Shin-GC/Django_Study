from django import forms
from .models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': '제목을 입력해주세요'}
            ),
            'dt_created': forms.DateTimeInput(
                attrs={'placeholder': '날짜를 입력해주세요'}
            ),
            'score': forms.NumberInput(
                attrs={'placeholder': '숫자만 입력해주세요.'}
            ),
            'feeling': forms.TextInput(
                attrs={'placeholder': '상태를 입력해주세요'}
            ),
            'content': forms.Textarea(
                attrs={'placeholder': '내용을 입력해주세요! (최소 10자 이상!)'}
            )
        }

