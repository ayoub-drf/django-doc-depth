from django.shortcuts import render


def index(request):

    context = {}
    return render(request, 'new_formsets/index.html', context)