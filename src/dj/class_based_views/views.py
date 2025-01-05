from typing import Any
from django.shortcuts import (
    render,
    HttpResponse
)
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    View,
    UpdateView,
    FormView,
    RedirectView,
    TemplateView,
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.utils.decorators import (
    method_decorator
)
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.urls import (
    reverse,
    reverse_lazy
)
from .forms import (
    MyForm,
    BookForm,
)
from .models import Book
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
)
from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    LoginRequiredMixin,
)

from django.views.generic.base import (
    TemplateResponseMixin,
    ContextMixin,
    View
)
from django.views.generic.detail import (
    SingleObjectMixin,
    SingleObjectTemplateResponseMixin, 
)
from django.views.generic.list import (
    MultipleObjectMixin,
    MultipleObjectTemplateResponseMixin
)
from django.views.generic.edit import (
    DeletionMixin,
    ProcessFormView,
    FormMixin,
)
from .mixins import CustomLoginRequiredMixin

my_mixins = (
    SingleObjectMixin,
    MultipleObjectMixin,
)

from django import forms
class MyBookForm(forms.Form):
    name = forms.CharField()


class MySingleObjectMixin(TemplateResponseMixin, View):
    queryset = Book.objects.all()
    template_name = "cbvS/index.html"

    
    def setup(self, request, *args, **kwargs):
        self.message = "Hello, world! =>"
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        
        # Comes from TemplateResponseMixin
        return self.render_to_response({'message': self.message})
    
    # def get(self, request, *args, **kwargs):
    #     context = {
    #         # Comes from MultipleObjectMixin
    #         'query': self.get_queryset()
    #     }
        
    #     return render(request, self.template_name, context)
    
    # def get(self, request, *args, **kwargs):
    #     context = {
    #         # Comes from SingleObjectMixin
    #         'obj': self.get_object()
    #     }
    #     return render(request, self.template_name, context)


class MyClassViewThree(CustomLoginRequiredMixin, TemplateView):
    template_name = "cbvS/index.html"


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "cbvS/index.html"

class CustomPasswordResetView(PasswordResetView):
    template_name = "cbvS/index.html"

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        if True:
            form.add_error('email', "exists")

            return self.form_invalid(form)
        print('An email has been sent to your email %s' % email)
        return super().form_valid(form)
    
class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "cbvS/index.html"

class CustomPasswordChangeView(PasswordChangeView):
    template_name = "cbvS/index.html"
 
class CustomLogoutView(LogoutView):
    template_name = "cbvS/index.html"

class CustomLoginView(LoginView):
    template_name = "cbvS/index.html"

    def get_redirect_url(self):
        return "/books/"


class BookListView(ListView):
    model = Book
    context_object_name = 'books' # default = object_list
    template_name = "cbvS/index.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['created'] = 2024
        return context
    
    def get_queryset(self):
        return Book.objects.filter(id__gt=3)  

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book' # default object
    template_name = "cbvS/index.html"
    

    def get_object(self, queryset = ...):
        return Book.objects.get(id=4)

class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    template_name = "cbvS/index.html"
    success_url = "success/"

    def form_valid(self, form):
        print('Form is valid')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.object.pk})

class BookUpdateView(UpdateView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            return JsonResponse({'msg': "Not allowed"})
        return super().dispatch(request, *args, **kwargs)

    model = Book
    fields = '__all__'
    template_name = "cbvS/index.html"
    # success_url = "success/"

    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = "overridden"
        return initial

class BookDeleteView(DeleteView):
    model = Book
    fields = '__all__'
    template_name = "cbvS/index.html"
    success_url = "success/"

class MyFormViewTwo(FormView):
    template_name = "cbvS/index.html"
    form_class = MyForm
    success_url = "/books/"

    def form_valid(self, form):
        # print(form.send_email(form.cleaned_data.get("email")))
        return super().form_valid(form)

class RedirectToHomeView(RedirectView):
    url = '/books/'


class ProtectedView(TemplateView):
    template_name = "cbvS/index.html"

    @method_decorator(login_required(login_url="/admin/"))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# class MyFormView(View):
#     form_class = MyForm
#     initial = {"name": "Dexter"}
#     template_name = "cbvS/index.html"

#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {"form": form})
    
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data.get('name'))
#             return HttpResponseRedirect("/success/")

#         return render(request, self.template_name, {"form": form})

decorators = [never_cache, csrf_exempt]

@method_decorator(decorators, name="dispatch")
class MyView(View):
    name = None
    def get(self, request):
        print(self.name)
        return JsonResponse({"method": request.method})
    def post(self, request):
        return JsonResponse({"method": request.method})
    def delete(self, request):
        return JsonResponse({"method": request.method})
    def put(self, request):
        return JsonResponse({"method": request.method})
    def patch(self, request):
        return JsonResponse({"method": request.method})
    

