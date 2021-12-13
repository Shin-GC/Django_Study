import random
from .models import Page


def validate_pages():
    pages = Page.objects.all()
    for page in pages:
        if 0 > page.score or page.score > 10:
            values = random.randint(0, 10)
            page.score = values
            page.save()
