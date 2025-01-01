from django.urls import path
from .views import (
    MyView,
    # MyFormView,
    ProtectedView,
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    MyFormViewTwo,
    RedirectToHomeView,
    CustomLoginView,
    CustomLogoutView,
    CustomPasswordChangeView,
    CustomPasswordChangeDoneView,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    MyClassViewThree,
    MySingleObjectMixin,
)

from django.contrib.auth.decorators import (
    login_required,
    permission_required
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', MySingleObjectMixin.as_view()),

    # path('', MyClassViewThree.as_view()),


    # path('reset-password/', CustomPasswordResetView.as_view()),
    # path('reset-password-done/', CustomPasswordResetDoneView.as_view(), name="password_reset_done"),




    # path('change-password/', CustomPasswordChangeView.as_view()),
    # path('logout/', LogoutView.as_view(), name="logout"),
    # path('change-password-done/', CustomPasswordChangeDoneView.as_view(), name="password_change_done"),


    # path('login/', CustomLoginView.as_view()),


    # path('', MyView.as_view(name="James")),

    # path('', login_required(MyFormView.as_view())),

    # path('books/', BookListView.as_view()),

    # path('books/<str:pk>/', BookDetailView.as_view(), name="Book-detail"),

    # path('books/', BookCreateView.as_view()),

    # path('books/<str:pk>/', BookUpdateView.as_view()),

    # path('books/<str:pk>/', BookDeleteView.as_view()),

    # path('books/', MyFormViewTwo.as_view()),

    # path('login/', LoginView.as_view(template_name="cbvS/index.html")),

]

