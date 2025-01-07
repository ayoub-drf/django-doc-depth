from django import forms

class MyForm(forms.Form):
    # template_name = "new_forms_1/form_snippet.html"
    name = forms.CharField(label="Name", max_length=100, help_text="NAME CANNOT BE a")

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if "a" in name:
            raise forms.ValidationError("Name contains inappropriate word!")

        return name
 