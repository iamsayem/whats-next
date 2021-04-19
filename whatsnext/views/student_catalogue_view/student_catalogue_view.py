"""
    Created by Sayem on 16 November, 2019
"""
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from ...models import ConsoleUser

__author__ = "sayem"


class StudentCatalogueView(ListView):
    def get_template_names(self):
        return ["pixel-html/index.html"]

    def get_queryset(self):
        return ConsoleUser.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        object_list = self.get_queryset()
        ctx = super(StudentCatalogueView, self).get_context_data(object_list=object_list, **kwargs)
        return ctx

    def get(self, request, *args, **kwargs):
        return render(
            request=request, template_name=self.get_template_names(),
            context=self.get_context_data(**kwargs)
        )

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(StudentCatalogueView, self).dispatch(*args, **kwargs)
