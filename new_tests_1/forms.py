from django import forms 

class MyForm(forms.Form):
    # image = forms.ImageField()
    file = forms.FileField()
    name = forms.CharField()
    age = forms.IntegerField()