from django import forms
from django.forms import (
    ModelForm,
    Form,
    modelform_factory,
    formset_factory,
    modelformset_factory,
    inlineformset_factory,
    BaseFormSet
)
from django.contrib.auth import get_user_model
User = get_user_model()

class BaseArticleFormSet(BaseFormSet):

    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields["my_field"] = forms.CharField(required=False)
    
    def clean(self):
        if any(self.errors):
            return 
        
        titles = set()
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue
            title = form.cleaned_data.get("title")
            if title in titles:
                raise forms.ValidationError("Articles in a set must have distinct titles.")
            titles.add(title)
    

class BookForm(Form):
    title = forms.CharField()
    user = forms.ModelChoiceField(queryset=User.objects.all())

    def __init__(self, *args, user, **kwargs):
        self.user = kwargs.get('user')
        super().__init__(*args, **kwargs)
    
BookFormSet = formset_factory(BookForm)

class ArticleForm(Form):
    title = forms.CharField()
    pub_date = forms.DateField()

# ArticleFormSet = formset_factory(ArticleForm, extra=2, max_num=2)
# ArticleFormSet = formset_factory(ArticleForm, extra=2)
ArticleFormSet = formset_factory(ArticleForm, formset=BaseArticleFormSet, max_num=1, validate_max=True)
