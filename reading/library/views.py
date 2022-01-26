from django.shortcuts import render, get_object_or_404
from .models import Books, Author
from django.contrib.auth.decorators import login_required

# Create your views here.
books = [
    {'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    {'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
    {'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
]

@login_required
def home(request):
    # data = { 'books': books }
    data = {'books': Books.objects.all()}
    return render(request, 'index.html', data)

@login_required
def show(request, id):
    # book = list(filter(lambda books: books['id'] == id, books))
    book = get_object_or_404(Books, pk=id)
    # data = {'book': book[0]}
    data = {'book': book}
    return render(request, 'show.html', data)

def not_found_404(request, exception):
    data = {'err': exception}
    return render(request, '404.html', data)

def server_error_500(request):
    return render(request, '500.html')