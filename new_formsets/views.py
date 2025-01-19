from django.shortcuts import render
from .forms import (
    ArticleFormSet,
    BookForm,
    BookFormSet
)
import datetime
from django.forms import formset_factory



def index(request):
    # initial = {
    #     "title": "Django is now open source",
    #     "pub_date": datetime.date.today(),
    # }
    
    # data = {
    #     "form-TOTAL_FORMS": "2",
    #     "form-INITIAL_FORMS": "0",
    #     "title": "Django is now open source",
    #     "pub_date": datetime.date.today(),
    # }
    # data = {
    #     "form-TOTAL_FORMS": "2",
    #     "form-INITIAL_FORMS": "0",
    #     "form-0-title": "Django is now open source",
    #     "form-0-pub_date": datetime.date.today(),
    #     "form-1-title": "Django is now open source",
    #     "form-1-pub_date": datetime.date.today(),
    # }
    # formset = ArticleFormSet(initial=[initial,])
    # formset = ArticleFormSet({}, error_messages={"missing_management_form": "Sorry, something went wrong."})

    # print(formset.is_valid())
    # print(formset.errors)
    # print(formset.non_form_errors())


    # data = {
    #     "form-TOTAL_FORMS": "1",
    #     "form-INITIAL_FORMS": "0",
    #     "form-0-title": "Test",
    #     "form-0-pub_date": "1904-06-16",
    #     # "form-1-title": "Test",
    #     # "form-1-pub_date": "1912-06-23",
    # }
    # formset = ArticleFormSet(data)
    # formset.is_valid()
    # print(formset.errors)
    # print(formset.non_form_errors())


    # for form in formset:
    #     print(form)

    form = BookFormSet(form_kwargs={"user": request.user})

    context = {
        # 'formset': formset,
        'formset': form,
    }
    return render(request, 'new_formsets/index.html', context)