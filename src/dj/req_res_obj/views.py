from django.db.models.fields.files import ImageField
from django.http import (
    JsonResponse,
    QueryDict,
    HttpResponse,
    HttpResponseRedirect,
    FileResponse
)
from django.template.response import (
    SimpleTemplateResponse,
    TemplateResponse
)
from io import BytesIO
import os
import subprocess
import xml.etree.ElementTree as ET
import copy

def index(request):
    # result = subprocess.run("ls media/x.png", shell=True, text=True, capture_output=True)
    # print(result.stdout)
    # with open("media/x.png", "rb") as file:
    #     request.FILES["image"] = BytesIO(file.read())
    #     img = ImageField(request.FILES["image"])
    #     print(img)


    # print("method", request.method)
    # print("COOKIES", request.COOKIES['sessionid'])
    # print("GET", request.GET.get('q'))
    # print("META", request.META)
    # print(request.POST)
    # print(request.accepted_types)
    # print(request.accepts)
    # print(request.auser)
    # print(request.body)
    # print(request.build_absolute_uri("api/"))
    # print(request.close)
    # print(request.content_params)
    # print(request.content_type)
    # print(request.encoding)
    # print(request.get_full_path())
    # print(request.get_full_path_info())
    # print(request.get_host())
    # print(request.get_port())
    # print(request.headers)
    # print(request.is_secure())
    # print(request.scheme)
    # print(request.user)
    # request.session['name'] = "dexter"
    # print(request.session.get('name'))
    # print(request.read())

    # it can be modified using mutable true
    # query = QueryDict(query_string="a=1&a=12&b=1&c=3", mutable=True)
    # print(query.getlist('a'))
    # print(query.get('c'))
    # print(query.keys())
    # print("c" in query)
    # query['x'] = 92

    # fromkeys_query = QueryDict.fromkeys(
    #     ["A", "B"],
    #     value=[1, 2],
    #     mutable=True
    # )
    # print(fromkeys_query.__getitem__("A"))
    # fromkeys_query.__setitem__("C", [3, 34])
    # print(fromkeys_query.__contains__("A"))
    # fromkeys_query.update({"A": 111})
    # print(list(fromkeys_query.items()))
    # print(list(fromkeys_query.values()))

    # res = HttpResponse(content=b'', content_type='text/html', status=200, reason=None, charset=None, headers=None)
    # res.write("<p>Here's the text of the web page.</p>")

    # res.set_cookie("id", value="Id454545", max_age=None, expires=None, path='/', domain=None, secure=False, httponly=False, samesite=None)

    redirect_res = HttpResponseRedirect(redirect_to="/login/")

    return HttpResponse()


def index_1(request):
    # res SimpleTemplateResponse('404.html', {"name": "Joss"})
    res = TemplateResponse(request, '404.html', {"name": "Joss"})
    return res