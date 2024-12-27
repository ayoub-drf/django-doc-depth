from django.urls import (
    path,
    re_path,
    include,
)


from . import views

app_name = "new_URLconfs"

# str int slug uuid

# from new_models import views as models_views

# extra_patterns = [
#     path('', models_views.index)
# ]


urlpatterns = [
    # named reqular expression ?P<name>pattern
    # Unnamed reqular expression ([0-9]{4})
    # re_path(r"^one/([A-z]+)/$", views.index_1), # NO RECOMMANDED

    # path("one/", views.index_1),
    # re_path(r"^one/(?P<name>[A-z]+)/$", views.index_1),

    # Include the urls from an External app
    # path("models/", include('new_models.urls')),

    # Alternative
    # path("models/", include(extra_patterns)),

    # path("", views.index_1),
    # path("<str:name>/", include(
    #     [
    #         path('1/', views.index_1),
    #         path('2/', views.index_2),
    #         path('3/', views.index_3),
    #     ]
    # ))

    # extra options
    # path("one/", views.index_1, {"foo": "james"}),

     # extra options to include
    # path("models/", include("new_models.urls"), {"foo": "james"}),

    path('one/', views.index, name="index"),

    path('one/<str:name>/', views.index_1, name="index-one"),

    # Nested arguments
    # re_path(r"^one/(?:page-(?P<name>[A-z0-9]+)/)?$", views.index_1),
]
