import logging

from django.utils.deprecation import (
    MiddlewareMixin,
)
from datetime import datetime
from django.core.exceptions import PermissionDenied


from asgiref.sync import iscoroutinefunction
from django.utils.decorators import sync_and_async_middleware


@sync_and_async_middleware
def simple_middleware_two(get_response):
    print(iscoroutinefunction(get_response))
    if iscoroutinefunction(get_response):
        async def middleware(request):
            response = await get_response(request)
            return response
    else:
        def middleware(request):
            response = get_response(request)
            return response
        
    return middleware

def simple_middleware(get_response):
    logger = logging.getLogger('middleware_1')

    def middleware(request):
        logger.info(f"request.method: {request.method}")

        res = get_response(request)

        res['X-Now'] = datetime.now()

        return res
    
    return middleware


class SimpeMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.NOW = datetime.now()
        if not request.user.is_authenticated:
            raise PermissionDenied("not is_authenticated")

        
        res = self.get_response(request)

        res['X-Now'] = datetime.now()

        return res

        

class LoggerViewMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('middleware_1')

    def __call__(self, request):
        self.logger.info("Hello from LoggerViewMiddleWare")

        res = self.get_response(request)

        return res
    
# Older | Deprecated 
# class LoggerViewMiddleWare(MiddlewareMixin):
#     def __init__(self, get_response = ...):
#         self.logger = logging.getLogger('middleware_1')

#         super().__init__(get_response)

#     def process_request(self, request):
#         self.logger.info("process_request")
#         print("#" * 33)

#     def process_response(self, request, response):
#         self.logger.info("process_response")

#         return response