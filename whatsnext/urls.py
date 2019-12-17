"""
    Created by Sayem on 12 October, 2019
"""

from django.conf.urls import url

from whatsnext.views import StudentCatalogueView
from .views import LoginAPIView, RegistrationAPIView

__author__ = "sayem"

urlpatterns = [
    url(
        regex=r'^api/login/$',
        view=LoginAPIView.as_view({'get': 'list', 'post': 'create'}),
        name="Login"
    ),
    url(
        regex=r'^api/register/$',
        view=RegistrationAPIView.as_view({'get': 'list', 'post': 'create'}),
        name="Registration"
    ),
    url(regex=r'^$', view=StudentCatalogueView.as_view(), name="student_catalogue"),
]
# urlpatterns += i18n_patterns(
#     url(regex=r'^$', view=StudentCatalogueView.as_view(), name="student_catalogue"),  # Django JET URLS
#     # url(r'^jet/dashboard/', include(arg='jet.dashboard.urls', namespace='jet-dashboard')),  # Django JET dashboard URLS
# )
