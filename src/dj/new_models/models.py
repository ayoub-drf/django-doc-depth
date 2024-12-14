from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# class CommonInfo(models.Model): # does not exists in db
#     name = models.CharField(max_length=100) 
#     created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         # if True all the models that inherit this class will have the same fields
#         abstract = True # The base class of my all models (name, created)

# class Person(CommonInfo):
#     slug = models.SlugField(null=True, blank=True)

#     def __str__(self):
#         return self.name
    
#     class Meta(CommonInfo.Meta): # Inherit the meta class from CommonInfo
#         db_table = "person_info" # make sure to Override the db_table

#     # class Meta(CommonInfo.Meta, AnotherClass.Meta): # Multiple Inheritance
#     #     db_table = "person_info"
    
#     # def save(self, *args, **kwargs):
#     #     if self.name == "james":
#     #         print('name cannot be james')
#     #         return
#     #     else:
#     #         self.name = self.name.upper()
#     #         super().save(*args, **kwargs)
#     #         print("name moved to UPPER")



#     # def delete(self, *args, **kwargs):
#     #     Person.objects.create(name=f"({self.name}) has been deleted")
#     #     super().delete(*args, **kwargs)



# class Group(CommonInfo):

#     # through keyword means that this member field is it going to take
#     # the person that match the group inside the Membership 
#     members = models.ManyToManyField(Person, through="Membership")

#     def __str__(self):
#         return self.name
    
#     # person.membership_set.all()


# class Membership(CommonInfo):
#     name = None # remove name from this class
#     person = models.ForeignKey(
#         Person, on_delete=models.CASCADE,
#         # %(app_label)s == the name of the app the contain this model (new_models)
#         # %(class) the name of this class Membership
#         related_name="%(app_label)s_%(class)s",
#     )
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)

# class Profile(Person):
#     is_active = models.BooleanField(default=True)



class Book(models.Model):
    # class YearInSchool(models.TextChoices):
    #     FRESHMAN = "FR", _("Freshman")
    #     SOPHOMORE = "SO", _("Sophomore")
    #     JUNIOR = "JR", _("Junior")
    #     SENIOR = "SR", _("Senior")
    #     GRADUATE = "GR", _("Graduate")

    name = models.CharField(max_length=100)
    pointes = models.IntegerField(default=1)

    # year_in_school = models.CharField(
    #     max_length=2,
    #     choices=YearInSchool,
    #     default=YearInSchool.FRESHMAN,
    # )
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)

    objects = models.Manager() # Default and Automatically added to a model

    class GreaterTheTenManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(pointes__gte=10)
        
    my_manager = GreaterTheTenManager()
    # class Meta:
        # verbose_name = "student"
        # verbose_name_plural = "students"
        # unique_together = ["first_name", "last_name"]
        # db_table = "custom_student"
        # db_table_comment = "Question answers"
        # get_latest_by = ["-created", "-updated"]
        # ordering = ["-created", ]
        # permissions = [("can_answer_q", "Can answer Questions")]
        # default_permissions = []
        # indexes = [
        #     models.Index(fields=["last_name", "first_name"]),
        #     models.Index(fields=["first_name"], name="first_name_idx"),
        # ]

