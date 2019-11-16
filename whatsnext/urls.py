"""
    Created by Sayem on 12 October, 2019
"""
import importlib

from django.conf import settings
from django.conf.urls import url

from whatsnext.views import StudentCatalogueView
from .decorators.decorators import get_models_with_decorator
from .views import LoginAPIView, RegistrationAPIView

__author__ = "sayem"

urlpatterns = []
INSTALLED_APPS = settings.PROJECT_APPS

all_models = get_models_with_decorator('expose_api', INSTALLED_APPS, include_class=True)
for _model in all_models:
    _view_cls = getattr(
        importlib.import_module(_model._meta.app_label + ".views", _model._registry.get("api_view")),
        _model._registry.get("api_view")
    )
    urlpatterns.append(
        url(
            regex=r'^api/' + _model._registry.get("api_url_postfix") + "/$",
            view=_view_cls.as_view({'get': 'list', 'post': 'create'}),
            name=_model.__name__
        )
    )
urlpatterns += [
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
