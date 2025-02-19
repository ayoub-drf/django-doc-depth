from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your views here.

from django.utils import translation


def welcome_translated(language):
    cur_language = translation.get_language()
    try:
        translation.activate(language)
        text = _("You people this is ayoub here from space")
    finally:
        translation.activate(cur_language)
    return text

def home_view(request):
    print(welcome_translated('it'))
    context = {
        'greeting': _("Welcome to our website!"),
        'current_date': timezone.now()
    }
    
    
    return render(request, 'new_internationalization/home.html', context)
