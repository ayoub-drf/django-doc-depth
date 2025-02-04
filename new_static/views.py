from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(req):

    # send_mail(
    # "Subject Here",
    # "Here is the message.",
    # "from@example.com",
    # ["to@example.com"],
    # fail_silently=False,
    # )
    
    return render(req, "new_staticx/index.html")