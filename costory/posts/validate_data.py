#
# import os
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "costory.settings")
# from django.core.wsgi import get_wsgi_application
#
# application = get_wsgi_application()
#
from posts.models import Post


# if __name__ == '__main__':
def validate_post():
    posts = Post.objects.all()
    for post in posts:
        if '&' in post.content:
            print(f"{post.id}번 글에 '&'가 들어가 있습니다.")
            post.content = post.content.replace('&', '')
            post.save()
        if post.dt_modified < post.dt_created:
            print(f"{post.id}번 글이 생성일 보다 수정일이 더 과거에 있습니다.")
            post.save()
