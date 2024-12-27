from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

def index(request):

    return HttpResponseRedirect(reverse_lazy('index-one', args=("James",)))

def index_1(request, name="Unknown"):
    # print(reverse('index-one', args=(name,)))
    print(reverse('new_URLconfs:index-one', args=("Maria",)))

    return HttpResponse("Hello %s" % name)

# def index_2(request, name="Unknown"):

#     return HttpResponse(f"Hello {name} | index_2")

# def index_3(request, name="Unknown"):

#     return HttpResponse(f"Hello {name} | index_3")
