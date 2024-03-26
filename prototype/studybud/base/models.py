from django.db import models
import uuid

class Author(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)   
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    genres = models.ManyToManyField('Genre', blank=True)
    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name

class BookDetails(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.book.title
    
class Matherial(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    '''def __str__(self):
        return self.name'''