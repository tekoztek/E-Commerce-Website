from django.contrib import admin

# Register your models here.
from .models import Author, Book, Genre, BookDetails, Matherial

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(BookDetails)
admin.site.register(Matherial)