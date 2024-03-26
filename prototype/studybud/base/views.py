from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book, Author


rooms = [
    {'id':1, 'name':'Lets learn Python'},
    {'id':2, 'name':'Lets learn Java'},
    {'id':3, 'name':'Lets learn Andro'}
]

author = Author.objects.get(name='Sam Emanuel')


# Create your views here.
def home(request):
    print(author.book_set.all())
    return render(request, 'main.html')

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
         
        context = {'room':room}
    return render(request, 'base/room.html', context)

def test1_view(request):
    return HttpResponse('test1 http responce')


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('Hello World')


