from django.shortcuts import render, HttpResponse
from .forms import ContactForm, FirstForm, CommentForm, ThirdFrom

def index(request):
    data = {
        "email": "x@aol.com"
    }
    f = ThirdFrom()
    context = {
        'form': f
    }
    return render(request, "new_form_api/index.html", context)

def index_1(request):
    if request.method == 'POST':
        pass

    form = ContactForm(data={"username": ""}, label_suffix=" =>")
    # form.is_valid()
    # print(form.cleaned_data)
    # print(form.as_div())
    # print(form.as_p())
    # print(form.errors.as_json())
    # print(form.errors.as_text())
    # print(form.has_changed())
    # print(form.fields['username'])
    # form.base_fields["username"].label_suffix = "?"
    # form.is_multipart()




    
    context = {
        'form': form
    }
    return render(request, "new_form_api/index.html", context)