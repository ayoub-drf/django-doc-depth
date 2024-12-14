from django.http import HttpResponse
# from .models import (
#     Person,
#     Group,
#     Membership,
# )
from datetime import date

def index(request):
    # Person.objects.create(name="Ringo Starr")
    # ringo = Person.objects.get(name="Ringo Starr")

    # Person.objects.create(name="Paul McCartney")
    # paul = Person.objects.get(name="Paul McCartney")

    # maria = Person.objects.get(name="maria")

    # Group.objects.create(name="The Beatles")
    # beatles = Group.objects.get(name="The Beatles")

    # m1 = Membership(
    #      person=ringo,
    #      group=beatles,
    #      date_joined=date(1962, 8, 16),
    #      invite_reason="Needed a new drummer.",
    # )
    # m1.save()

    # group_members = beatles.members.all()
    # person_groups = ringo.group_set.all()


    # group_add_new_person_paul = beatles.members.add(
    #     paul,
    #     through_defaults={
    #         'group': beatles,
    #         'date_joined': date(1962, 8, 16),
    #         'invite_reason': "Needed a new drummer."
    #     }
    # )
    
    # group_create_new_person_dexter = beatles.members.create(
    #     name="dexter",
    #     through_defaults={
    #         'group': beatles,
    #         'date_joined': date(1962, 8, 16),
    #         'invite_reason': "Needed a new drummer."
    #     }
    # )

    # group_set_multiple_persons = beatles.members.set(
    #     [paul, maria],
    #     through_defaults={
    #         'group': beatles,
    #         'date_joined': date(1962, 8, 16),
    #         'invite_reason': "Needed a new drummer."
    #     }
    # )

    # group_remove_maria = beatles.members.remove(maria)

    # clear_all_persons = beatles.members.clear()

    # groups_contains_maria_member = Group.objects.filter(members__name__startswith="maria")

    # print(ringo.membership_set.all()) # To access memberships related to ring person

    # persons inside group beatles and their membership invite reason is Needed a new drummer.
    # inside_beatles_membership_invite_reason = Person.objects.filter(
    #     group__name="The Beatles",
    #     membership__invite_reason__icontains="Needed a new drummer.",
    # )


    return HttpResponse('Hello world')