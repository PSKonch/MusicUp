from typing import Any
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest
from django.contrib.auth import get_user_model
 
class EmailAuthBackend(BaseBackend):
    def authenticate(self, request: HttpRequest, username: str, password: str, **kwargs: Any):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except:
            return (user_model.DoesNotExist ,user_model.MultipleObjectsReturned)
