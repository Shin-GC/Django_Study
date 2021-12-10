from django import forms
from .models import Post
from .validators import validate_symbols


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {'title': forms.TextInput(attrs={'class': 'title',
                                                   'placeholder': '제목을 입력 하세요.'}),
                   'content': forms.Textarea(attrs={'class': 'content',
                                                    'placeholder': '내용을 입력 하세요.'})}
