from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from .models import Article

# @admin.action(description="Mark selected stories as published")
# def make_published(modeladmin, request, queryset):
#     queryset.update(status="p")
    
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ["title", "status"]
#     ordering = ["title"]
#     actions = [make_published]
    
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]
    ordering = ["title"]  
    actions = ["make_published"]

    def make_published(self, request, queryset):
        updated = queryset.update(status="p")
        self.message_user(
            request,
            ngettext(
                "%d story was successfully marked as published.",
                "%d stories were successfully marked as published.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

# admin.site.disable_action("make_published")

admin.site.register(Article, ArticleAdmin)