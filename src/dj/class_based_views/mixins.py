import logging
from django.http import HttpResponseRedirect

logger = logging.getLogger('class_based_views')

class CustomLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            logger.info("Login required to access this view")
            return HttpResponseRedirect('/admin/')

        return super().dispatch(request, *args, **kwargs)