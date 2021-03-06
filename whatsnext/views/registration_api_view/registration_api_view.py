"""
    Created by Sayem on 15 October, 2019
"""
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from enginecore.utils import Clock
from whatsnext.models import ConsoleUser

__author__ = "sayem"


class RegistrationAPIView(ModelViewSet):
    def create(self, request, *args, **kwargs):
        """
        This method is to register a new user if it itself does not exist. Besides, if the picked
        username from the mobile application exists in the database, it will handle this
        kind of exception for this case as well. After a successful registration it will respond to
        that new user to get logged in the mobile application based on valid `token` authentication.
        :param request: Request data sent from the mobile application.
        :param args: Sent arguments paired value in tuple format.
        :param kwargs: Sent keyword argument paired value in dictionary format.
        :return: Returns response based on success/failure.
        """
        try:
            _data = request.data
            if _data:
                if User.objects.filter(username=_data.get("username")).count():
                    return Response(data={
                        "message": "Invalid Username!!! Please choose another one.",
                        "success": False
                    },
                        status=status.HTTP_409_CONFLICT,
                        content_type="application/json"
                    )
                _django_auth_user = User(
                    username=_data.get("username"),
                    first_name=_data.get("first_name"),
                    last_name=_data.get("last_name"),
                    email=_data.get("email")
                )
                _django_auth_user.set_password(raw_password=_data.get("password"))
                _django_auth_user.save()
                _console_user = ConsoleUser(
                    user=_django_auth_user,
                    phone=_data.get("phone", None),
                    date_of_birth=Clock.convert_str_to_date_obj(date_str=_data.get("date_of_birth")) if _data.get(
                        "date_of_birth") else None
                )
                _console_user.save()
                _token, _created = Token.objects.get_or_create(user=_django_auth_user)
                return Response(
                    data={
                        "token": _token.key,
                        "message": "Request processed successfully.",
                        "result": [_console_user.to_dict()],
                        "success": True
                    },
                    status=status.HTTP_200_OK,
                    content_type="application/json"
                )
            return Response(
                data={
                    "message": "Request contains no content",
                    "success": False
                },
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json"
            )
        except Exception as exp:
            return Response(
                data={
                    "message": str(exp),
                    "success": False
                },
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json"
            )
