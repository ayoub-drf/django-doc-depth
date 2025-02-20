from django.shortcuts import render
from django.utils import timezone

import pytz

def current_time(request):
    print(pytz.common_timezones)
    # timezone.activate(pytz.timezone('America/New_York'))
    context = {'current_time': timezone.now()}
    return render(request, 'new_Localization/home.html', context)
