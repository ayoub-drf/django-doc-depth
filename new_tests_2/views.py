from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "new_tests_2/home.html"

    def get_context_data(self, **kwargs):
        kwargs["environment"] = "Production"
        return super().get_context_data(**kwargs)

def index(request):

    return HttpResponse("def index(request):")

def index_1(request):

    return HttpResponse("index_1")

class Index2(View):
    def get(self, request, *args, **kwargs):

        return HttpResponse("Index2")
