from django.shortcuts import render
from .forms import BookForm, BookFormTwo, BookFormThree
from django.contrib.auth import get_user_model
from .models import Book, Author
User = get_user_model()

def index(request):
    # form = BookForm()
    # form = BookFormTwo()

    initial = {
        'name': "The book",
        'user': User.objects.latest('-date_joined'),
        'authors': [Author.objects.first(), Author.objects.last()]
    }
    data  = initial.copy()
    # data['name'] = f"{data['name']} UPDATED"
    data['name'] = f"test"

    form = BookForm(data=data, initial=initial)

    if form.is_valid():
        print(form.cleaned_data.get('name'))

        # new_book = form.save(commit=False)
        # new_book.user = User.objects.get(username="dexter")
        # new_book.save()

        # form.save_m2m() # Calling save_m2m() is only required if you use save(commit=False).
    else:
        print(form.errors.as_data())


    context = {
        # 'form': form,
        'form': BookFormThree,

    }
    return render(request, 'new_form_model/index.html', context)