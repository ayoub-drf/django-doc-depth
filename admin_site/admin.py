from django.contrib import admin
from .models import Book, Author, Publisher
from django.utils.timesince import timesince



class MyAdminSite(admin.AdminSite):
    site_header = "Monty Python administration"


admin_site = MyAdminSite(name="myadmin")
admin_site.register(Author)

from django import forms
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'published_date', 'description', 'price']


class PublisherInline(admin.TabularInline):
    model = Book.publisher.through  # Using the through table for many-to-many relationships
    extra = 0

class BookInline(admin.TabularInline):  
    model = Book
    extra = 1 

@admin.register(Author)
class AuthorInline(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [BookInline]


@admin.display(description="Title")
def upper_case_book_title(obj):
    return f"{obj.title}".upper()

# @admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'price', 'author__name')
    # show_facets = admin.ShowFacets.ALWAYS
    # raw_id_fields = ["author",]

    search_fields = ('title',)

    save_as= True


    # def get_search_fields(self, request):
    #     return ('id', )

    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request,
            queryset,
            search_term,
        )
        try:
            search_term_as_str = str(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(title=search_term_as_str)


        return queryset, may_have_duplicates
    
    def get_ordering(self, request):
        return ['-title']


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = (upper_case_book_title, 'author_name', 'author__created', 'colored_title', 'born_in_fifties', "__str__", 'display_publisher', 'view_description', 'published_date_period', 'price')
    list_display_links = ["author_name", "__str__"]
    inlines = [PublisherInline]
    search_fields = ['title', 'author']
    list_select_related = ["author",]

    @admin.display(ordering="author__name")
    def author_name(self, obj):
        return obj.author.name.upper()

    # list_filter = ('published_date', )

    # ordering = ['published_date']

    # list_editable = ('price',)

    # fields = (('title', 'published_date'), 'author')

    # exclude = ["author", ]

    # empty_value_display = "-empty-"

    @admin.display(description="period")
    def published_date_period(self, obj):
        return f'{timesince(obj.published_date)} ago'

    @admin.display(empty_value="-empty-")
    def view_description(self, obj):
        return obj.description
    
    fieldsets = (
        ('Book info', {
            'fields': ('title', 'author', 'price')
        }),
        ('Publishers', {
            "fields": ('publisher', )
        }),
        ('Publication Details', {
            'description': "Hello world",
            'fields': ('published_date', ),
            'classes': ['wide', 'collapse']
        }),
    )

    def display_publisher(self, obj):
        return ", ".join([p.name for p in obj.publisher.all()])
    display_publisher.short_description = 'Publishers'

    form = BookForm


admin.site.register(Publisher)
