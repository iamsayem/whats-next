"""
    Created by Sayem on 29 November, 2019
"""
from crequest.middleware import CrequestMiddleware
from django.apps import apps
from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed

__author__ = "sayem"


class TokenAuthenticationMixin(TokenAuthentication):
    """
    This class is for authenticating the token from the client side during an API request.
    """

    def authenticate(self, request):
        """
        Here the `authenticate` method has been overriden due to check the token requested by the user
        in order to identify whether the token is valid for the requested user or not.
        :param request: The WSGI request sent from the client/mobile side.
        :return: It returns the authenticated user and its token to the django rest framework if valid.
        """
        auth = get_authorization_header(request=request).split()

        if not auth or len(auth) == 0 or auth[0].lower() != b'token':
            return None

        if len(auth) <= 1:
            raise AuthenticationFailed(detail="Invalid token header. No credentials provide.")
        elif len(auth) > 2:
            raise AuthenticationFailed(detail="Invalid token header. Token string should not contain spaces.")

        """Retrieve the `User` by authenticating the received `Token` in auth[1]"""
        _token = self.get_model().objects.filter(key=auth[1].decode(encoding="utf-8")).first()
        if not _token:
            raise AuthenticationFailed(detail="Invalid Token")
        elif not (_token and _token.user and _token.user.is_active):
            raise AuthenticationFailed(detail="User inactive or deleted.")
        ConsoleUser = apps.get_model(app_label="enginecore", model_name="ConsoleUser")
        c_user = ConsoleUser.objects.get(user=_token.user)

        request.c_user = c_user

        CrequestMiddleware.set_request(request=request)
        return _token.user, _token.key
