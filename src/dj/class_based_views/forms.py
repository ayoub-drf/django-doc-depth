from django import forms


from .models import Book

class BookForm(forms.ModelForm):
    class Mata:
        model = Book
        fields = ('name', )

class MyForm(forms.Form):
    email = forms.CharField(max_length=200)

    def send_email(self, email):
        print(f"Email has been sent to {email}")

