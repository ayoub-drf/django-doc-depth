from django.shortcuts import render
from .forms import *

def index(request):
    form = EventForm()
    # context = {
    #     'form': EventForm
    # },

    return render(request, "form_integrating_media/index.html", {'form': form})
