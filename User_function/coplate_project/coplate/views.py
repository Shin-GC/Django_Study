from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView


def index(request):
    print(request.user.is_authenticated)
    return render(request, 'coplate/index.html')


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):  # 어떠한 폼이 성공적으로 처리되면 어디로 리디렉션 될지 정해주는 함수
        return reverse("index")
