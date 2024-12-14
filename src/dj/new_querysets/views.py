from django.shortcuts import render
from django.http import HttpResponse
from .models import (
    Blog,
    Author
)
from django.db.models import F

from django.db import transaction
from django.db.models import F, Avg, Min, Max, Count
# imports the F expression, which allows referencing and performing operations
# on model field values directly in database queries.
# Entry.objects.filter(number_of_comments__gt=F("number_of_pingbacks") * 2)

# result = Book.objects.aggregate(
#     total_books=Count('id'),      # Count the total number of books
#     avg_price=Avg('price'),       # Calculate the average price of all books
#     earliest_pub_date=Min('pub_date')  # Find the earliest publication date
# )

def index(request):
    # blog = Blog.objects.aggregate(
    #     total_blogs=Count("id"),
    #     min_blog=Min("id"),
    #     max_blog=Max("id"),
    #     average_blog=Avg("id"),
    # )


    # annotate allows to add extra attribute to you querysets
    # can the count of blogs of each author using annotate
    # blogsCount_forAuthor = [f'This Author {author.id} has {author.number_of_blogs} blogs.'
    #             for author in Author.objects.annotate(number_of_blogs=Count("blogs"))]
    
    # print(Author.objects.order_by('-id'))

    # union() for combine multiple querysets
    # print(Author.objects.all().union(Author.objects.all(), all=True))


    # Select_related() used for retrieving the related models without hit the database
    # ForeignKey and One-to-One
    # print(Blog.objects.select_related("author").get(id=1).author.name) # not hit for db

    # prefetch_related() used for reducing the numbers of queries on the db by fetching all related objects in a single query
    # ForeignKey and One-to-One and Many-To-Many
    # print(Blog.objects.prefetch_related("author").get(id=1).author.name) # not hit for db

    # defer() used when you want to don't fetch the author at this time for lazy_load
    # the author does not fetched immediately until you access it
    # print(Blog.objects.defer('author').get(id=1))

    # only() allows to limit the fields from your models here we fetch only the name
    # print(Blog.objects.only('name'))

    # using() allows you to select a query from which the database you want by access it name
    # print(Blog.objects.all()) # select all Blogs from the default db
    # print(Blog.objects.using('database_2').all()) # select all Blogs from the database_2

    # select_for_update() allows to lock the rows from db that you want to update  
    # It means that no other db transactions for this rows until your transaction end
    # with transaction.atomic():
    #     blog_1 = Blog.objects.select_for_update().get(id=1)
    #     blog_1.name = "Blog 1 updated"


    # raw() allows to execute sql and it's not safe also use it just for complex ORM
    # print([i.id for i in Blog.objects.raw("SELECT * FROM new_querysets_blog")])

    # create() for creating objects it auto save (no obj.save() required to save the object)
    # print(Blog.objects.create(name="test blog"))

    # obj() for creating objects it not auto save (obj.save() is required to save the obj)
    # print(Blog(name="test blog 2").save())

    # get_or_create() if there is a blog with the name Bob it's going to get it otherwise created
    # print(Blog.objects.get_or_create(name="Bob", defaults={"name": "Bob"}))

    # print(callable(x)) check if the object is callable like fun()

    # update_or_create() update the model if exists otherwise created
    # print(Blog.objects.update_or_create(name="Maria", defaults={"author": Author.objects.get(id=1)}))

    # Create multiple models
    # print(Blog.objects.bulk_create([Blog(name="x"), Blog(name="x"), Blog(name="x"),]))

    # bulk_update() update all filtered models in one single query just one update query for all the changes
    # print(Blog.objects.bulk_update(Blog.objects.filter(name="x"), ["name"]))

    # Count the models instances
    # print(Blog.objects.count())

    # fetch bulk objects by their ids
    # print(Blog.objects.in_bulk([1, 10, 11, 2]))

    # iterator() allows to iterate over query without loading all data into memory at ones
    # print([i for i in Blog.objects.all().iterator()])

    # Get the last and first objects
    # print(Blog.objects.last())
    # print(Blog.objects.first())

    # Get the latest and earliest objects
    # print(Blog.objects.latest('created'))
    # print(Blog.objects.earliest('created'))

    # aggregate() allows to compute summary values like (Avg, Max, Count)
    # print(Blog.objects.aggregate(max_id=Max("id")))

    # Check if object is exists
    # print(Blog.objects.filter(name="Maria").exists())

    # contains() check if specified objects contains inside a queryset
    # print(Blog.objects.contains(Blog.objects.get(id=1)))

    # Bulk update
    # print(Blog.objects.filter(name__contains="Maria").update(name="Maria Updated"))

    # Bulk delete
    # print(Blog.objects.filter(name__icontains="blog").delete())

    # Explain how django orm is going to execute this query
    # print(Blog.objects.filter(name__icontains="Blog").explain())



    return HttpResponse()

