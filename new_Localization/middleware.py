from django.utils import timezone
import pytz

class TimezoneMiddleware:
    """
    A middleware that activates the user’s time zone if set.
    In this demo, we assume that if the user is authenticated,
    a 'time_zone' attribute exists on the user object.
    """
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
                    timezone.deactivate()  # fallback to default if unknown
            else:
                timezone.deactivate()  # No custom time zone; use default
        else:
            timezone.deactivate()  # Not logged in, so use default (UTC)

        response = self.get_response(request)
        return response
