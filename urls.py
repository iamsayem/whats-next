"""WhatsNext URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import importlib

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve
from rest_framework.routers import SimpleRouter

from enginecore.decorators import get_models_with_decorator
from enginecore.mixin import GenericApiViewSetMixin

urlpatterns = list()
INSTALLED_APPS = settings.PROJECT_APPS

for _app in INSTALLED_APPS:
    try:
        _url_module = importlib.import_module(_app + '.urls')
        _app_urls = getattr(_url_module, 'urlpatterns')
        urlpatterns += _app_urls
    except ImportError as exp:
        pass

INSTALLED_APPS = settings.PROJECT_APPS

router = SimpleRouter()
all_models = get_models_with_decorator('expose_api', INSTALLED_APPS, include_class=True)
for _model in all_models:
    viewset_subclass = type(
        'RunTime_' + _model.__name__ + '_ViewSet',
        (GenericApiViewSetMixin,),
        dict(
            model=_model,
            serializer_class=_model.get_serializer())
    )
    router.register(prefix=r'api/' + _model._url_prefix, viewset=viewset_subclass, base_name=_model.__name__)

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
# ------------------------- general routes end -----------------------------------------

# urlpatterns += static(settings.STATIC_UPLOAD_URL, document_root=settings.STATIC_UPLOAD_ROOT)

# ------------------------- upload directory shortcut url --------------------------------------------

# static file urls
urlpatterns += i18n_patterns(
    url(r'^static/' + '(.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
    }),
    url(r'^static-media/' + '(.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
    }),
)
