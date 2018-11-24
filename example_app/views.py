from django.shortcuts import render
from django.views.generic import TemplateView
from django_q.tasks import async_task
# Create your views here.

class TopView(TemplateView):
    template_name = "example_app/top.html"

    def dispatch(self, request, *args, **kwargs):
        async_task("example_app.tasks.log_save", request.META["HTTP_USER_AGENT"])
        return super(TopView, self).dispatch(request, *args, **kwargs)
