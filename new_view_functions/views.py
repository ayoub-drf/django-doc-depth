from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseNotAllowed,
    HttpResponseNotFound,
    Http404,
    JsonResponse
)

import datetime
import httpx
import asyncio
from string import (
    ascii_lowercase,
    ascii_uppercase,
)

async def asynfunc_one():
    for i in ascii_uppercase:
        print(i)
        await asyncio.sleep(1)

async def asynfunc_two():
    for i in ascii_lowercase:
        print(i)
        await asyncio.sleep(1) 


async def get_posts(request):
    url = "https://jsonplaceholder.typicode.com/posts/"

    async with httpx.AsyncClient() as client:
        res = await client.get(url)

    await asyncio.gather(asynfunc_two(), asynfunc_one())


    # res = requests.get(url)

    return JsonResponse(res.json(), safe=False)


def index_1(request):
    now = datetime.datetime.now()
    context = {
        'name': "dexter"
    }
    html = f'''
        <html lang="en">
            <title>{now}</title>
            <body>It is now ${now}.</body>
        </html>
    
    '''
    raise  Http404("Poll does not exist")
    # return HttpResponse(html)
    # return HttpResponseNotAllowed(400)
    # return HttpResponseNotFound("Page not found")
    # return render(request, 'new_view_functions/index.html', context)
