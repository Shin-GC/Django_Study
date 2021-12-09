from django.core.exceptions import ValidationError


def validate_no_hash(value):
    if "#" in value:
        raise ValidationError("'#'은 내용에 포함될 수 없습니다.", code='symbol-err')


def validate_no_numbers(value):
    for v in value:
        if v.isdigit() is True:
            raise ValidationError("'감정상태'에는 숫자가 들어갈 수 없습니다.", code='emotion-err')
        else:
            pass


def validate_score(value):
    if 0 <= value <= 10:
        pass
    else:
        raise ValidationError("'감정점수'에는 0부터 10사이의 '숫자'만 들어갈 수 있습니다.", code='score-err')
