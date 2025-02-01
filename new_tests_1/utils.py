from django.db import transaction
from .models import Animal

def transaction_view(name, sound):
    with transaction.atomic():
        animal = Animal.objects.create(
            name=name,
            sound=sound
        )
    return animal