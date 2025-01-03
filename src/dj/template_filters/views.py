from django.shortcuts import render



def index(request, pk=None):

    context = {
        "my_list": ["Apple", "Banana", "Orange", "Grapes"]
    }

    return render(request, "template_filters/main.html", context)
