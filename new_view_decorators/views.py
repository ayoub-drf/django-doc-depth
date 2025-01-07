from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)
from django.contrib.admin.views.decorators import (
    staff_member_required,
)
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
    require_GET,
)
from django.views.decorators.cache import (
    cache_page,
    cache_control,
)
from django.views.decorators.common import (
    no_append_slash,
    wraps,
)
from django.views.decorators.gzip import (
    gzip_page
)
from django.views.decorators.csrf import (
    csrf_exempt
)
from django.views.decorators.vary import (
    vary_on_cookie,
    vary_on_headers
)

import time
from functools import wraps

def login_req(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        
        return HttpResponse("Login required")

    return wrapper


# @login_required(login_url='admin/')
# @permission_required("new_aggregation.can_add_book")
# @staff_member_required
# @require_http_methods(["GET"])
# @require_POST
# @require_GET
# @cache_page(60 * 60)
# @csrf_exempt
# @login_req
# @gzip_page
# @no_append_slash
def index(request):
    # time.sleep(5)
    # print(request.user.has_perms(["new_aggregation.can_add_book",]))
    # print(request.user.is_staff)

    data = "A large amount of data" * 1000

    return HttpResponse(data)