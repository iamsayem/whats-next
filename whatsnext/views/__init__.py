"""
    Created by Sayem on 15 October, 2019
"""
from .login_api_view.login_api_view import LoginAPIView
from .registration_api_view.registration_api_view import RegistrationAPIView
from .student_catalogue_view.student_catalogue_view import StudentCatalogueView

__author__ = "sayem"

__all__ = [
    "LoginAPIView",
    "RegistrationAPIView",
    "StudentCatalogueView"
]
