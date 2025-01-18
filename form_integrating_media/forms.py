from django import forms

class CalendarWidget(forms.TextInput):
    class Media:
        extend = False
        css = {
            "all": ["css/pretty.css"],
        }
        js = ["js/animations.js", "js/actions.js"]

    def __init__(self, attrs=None):
        super().__init__(attrs)
        if attrs:
            attrs.setdefault("class", "calendar-widget")
        else:
            attrs = {"class": "calendar-widget"}
        self.attrs = attrs

class EventForm(forms.Form):
    date = forms.DateField(widget=CalendarWidget(attrs={"placeholder": "YYYY-MM-DD"}))
