from django.core.exceptions import ValidationError
import string


def contains_special_character(value):
    for char in value:
        if char in string.punctuation:
            return True
    return False


def contains_uppercase_letter(value):
    for char in value:
        if char.isupper():
            return True
    return False


def contains_lowercase_letter(value):
    for char in value:
        if char.islower():
            return True
    return False


def contains_number(value):
    for char in value:
        if char.isdigit():
            return True
    return False


def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자는 포함 할 수 없습니다")


class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
                len(password) < 8
                or not contains_uppercase_letter(password)
                or not contains_lowercase_letter(password)
                or not contains_number(password)
        ):
            raise ValidationError("8자 이상의 영문 대/소문자, 숫자, 특수문자를 포함해야 합니다.!!")

    def get_help_text(self):
        return "8자 이상의 영문 대/소문자, 숫자, 특수문자를 포함해야 합니다."


# class CustomNicknameValidator:
#     def validate(self, nickname, user=None):
#         if not contains_special_character(nickname):
#             raise ValidationError("닉네임에는 특수문자가 들어가서는 안됩니다.")
#
#     def get_help_text(self):
#         return "닉네임에는 특수문자가 들어가서는 안됩니다."
#
#
# class CustomKakaoValidator:
#     def validate(self, kakao_id, user=None):
#         if not contains_special_character(kakao_id):
#             raise ValidationError("kakao_id 에는 특수문자가 들어가서는 안됩니다.")
#
#     def get_help_text(self):
#         return "kakao_id 에는 특수문자가 들어가서는 안됩니다."
#
#
# class CustomAddressValidator:
#     def validate(self, address, user=None):
#         if not contains_special_character(address):
#             raise ValidationError("주소에는 특수 문자가 들어갈 수 없습니다.")
#
#     def get_help_text(self):
#         return "주소에는 특수 문자가 들어갈 수 없습니다."
