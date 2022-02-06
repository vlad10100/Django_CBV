from django.contrib import admin

from .models import Book

@admin.register(Book)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} # why there s a comma??