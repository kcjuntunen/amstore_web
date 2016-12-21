from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib import messages

def index(*args):
    return HttpResponse(b'<html><title>Hay</title>Hey</html>')

class HomePageView(TemplateView):
    template_name = 'templates/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'Hello World')
        return context
