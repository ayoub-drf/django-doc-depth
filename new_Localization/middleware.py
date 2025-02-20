from django.utils import timezone
import pytz

class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            print('is_authenticated')
            user_tz = 'America/New_York'
            # user_tz = 'Europe/Paris'
            print('user_tz', user_tz)
            if user_tz:
                try:
                    tz = pytz.timezone(user_tz)
                    timezone.activate(tz)
                except pytz.UnknownTimeZoneError:
                    timezone.deactivate()
            else:
                timezone.deactivate()
        else:
            timezone.deactivate()

        response = self.get_response(request)
        return response
