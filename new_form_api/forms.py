from django import forms
import datetime
from .models import Comment, Post, Profile


class CommentForm(forms.Form):
    post = forms.ModelChoiceField(queryset=Post.objects.all(), label="Select Post", empty_label="(select-post)")
    commenter = forms.ModelChoiceField(queryset=Profile.objects.all(), label="Select Profile")
    # commenter = forms.ModelMultipleChoiceField(queryset=Profile.objects.all(), label="Select Profile")
    text = forms.CharField(max_length=200, label="Your Comment")

class ContactForm(forms.Form):
    error_css_class = "error"
    required_css_class = "required"
    username = forms.CharField(max_length=100)

class SecondForm(ContactForm):
    username = None
    email = forms.EmailField()

class FirstForm(forms.Form):
    CHOICES = [
        ("fr", "France"),
        ("it", "Italy"),
    ]
    json_field = forms.JSONField()
    multiple_choices = forms.MultipleChoiceField(choices=CHOICES)
    image_field = forms.ImageField()
    file_field = forms.FileField()
    name = forms.CharField(error_messages={"required": "Please enter your name"})
    email = forms.EmailField(label_suffix=' :', help_text="Enter your email",
                             widget=forms.EmailInput(attrs={
                                 'placeholder': "Enter your email"
                             }))
    url = forms.URLField(initial="https://")

    select_one = forms.ChoiceField(choices=CHOICES)
    available = forms.BooleanField()
    date = forms.DateField(initial=datetime.datetime.now)
    time = forms.TimeField(initial=datetime.datetime.now)
    date_time = forms.DateTimeField(initial=datetime.datetime.now)
    decimal_field = forms.DecimalField(decimal_places=2, max_digits=9)

BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
FAVORITE_COLORS_CHOICES = {
    "blue": "Blue",
    "green": "Green",
    "black": "Black",
}

class ThirdFrom(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={"class": "special"}))
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
    )
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

    comment.widget.attrs.update({"data-type": "xpx"})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs.update({"data-type": "xpx updated"})