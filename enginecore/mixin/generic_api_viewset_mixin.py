"""
    Created by Sayem on 29 November, 2019
"""
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import BrowsableAPIRenderer

from .token_authentication_mixin import TokenAuthenticationMixin
from ..utils import GenericJsonRenderer

__author__ = "sayem"


class GenericApiViewSetMixin(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthenticationMixin, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (GenericJsonRenderer, BrowsableAPIRenderer)
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        # log = ApiCallLog.log(request=request, log_time=True)
        # if log:
        #     self._log_tsync_id = log.tsync_id
        return super(GenericApiViewSetMixin, self).dispatch(request=request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        # _log_tsync_id = None
        # if hasattr(self, '_log_tsync_id'):
        #     _log_tsync_id = self._log_tsync_id
        # log = ApiCallLog.log(request=request, response=response, tsync_id=_log_tsync_id, log_time=False)
        # if log:
        #     self._log_tsync_id = log.tsync_id
        return super(GenericApiViewSetMixin, self).finalize_response(
            request=request, response=response, *args, **kwargs)

    def metadata(self, request):
        ret = super(GenericApiViewSetMixin, self).metadata(request)
        return ret

    def create(self, request, *args, **kwargs):
        # _log_tsync_id = None
        # if hasattr(self, '_log_tsync_id'):
        #     _log_tsync_id = self._log_tsync_id
        # log = ApiCallLog.log(request=request, tsync_id=_log_tsync_id)
        # if log:
        #     self._log_tsync_id = log.tsync_id
        return super(GenericApiViewSetMixin, self).create(request=request, *args, **kwargs)

    def update(self, request, *args, partial=True, **kwargs):
        # _log_tsync_id = None
        # if hasattr(self, '_log_tsync_id'):
        #     _log_tsync_id = self._log_tsync_id
        # log = ApiCallLog.log(request=request, tsync_id=_log_tsync_id)
        # if log:
        #     self._log_tsync_id = log.tsync_id
        return super(GenericApiViewSetMixin, self).update(request=request, *args, partial=partial, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(GenericApiViewSetMixin, self).partial_update(request=request, *args, **kwargs)

    def options(self, request, *args, **kwargs):
        return super(GenericApiViewSetMixin, self).options(request=request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(GenericApiViewSetMixin, self).destroy(request=request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        response = super(GenericApiViewSetMixin, self).list(request=request, *args, **kwargs)
        return response

    def get_queryset(self, **kwargs):
        queryset = super(GenericApiViewSetMixin, self).get_queryset(**kwargs)
        # queryset = super(GenericApiViewSetMixin, self).get_api_queryset(queryset=queryset, **kwargs)
        return queryset
