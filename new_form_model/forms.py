from django import forms

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import Book, Author
User = get_user_model()

# BookFormThree = forms.modelform_factory(Book, fields="__all__", widgets={"name": forms.Textarea()})
BookFormThree = forms.modelform_factory(Book, fields="__all__")
BookFormset = forms.formset_factory(BookFormThree, extra=2, can_delete=True)

class MyCharField(forms.CharField):
    def validate(self, value):
        super().validate(value)

        if 'test' in value.lower():
            raise forms.ValidationError("Invalid name")

def validate_name(value):
    if 'test' in value.lower():
        raise forms.ValidationError("Invalid name")
    return value

class BookForm(forms.ModelForm):
    name = forms.CharField(validators=[validate_name])

    class Meta:
        model = Book
        fields = ('name', 'user', 'authors')
        # exclude = ["name", ]
        # field_classes = {
        #     "name": MyCharField,
        # }
        # widgets = {
        #     'name': forms.Textarea(attrs={"cols": 22, "rows": 2})
        # }
        # labels = {
        #     'name': _("What is the name of the book")
        # }
        # help_texts = {
        #     "name": _("Name length must be less than 100 characters."),
        # }
        # error_messages = {
        #     "name": {
        #         "max_length": _("This name is too long."),
        #     },
        # }




class BookFormTwo(forms.Form):
    name = forms.CharField(max_length=100)
    user = forms.ModelChoiceField(queryset=User.objects.all())
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
