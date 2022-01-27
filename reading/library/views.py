from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Books, Author
from .forms import NewBookForm, AssignOwnerForm, RemoveOwner

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
def create(request):
    if request.method == "POST":
        book = NewBookForm(request.POST)
        if book.is_valid():
            id = book.save().id
            return redirect("library-show", id=id)
    else:
        form = NewBookForm()
    data = {'form': form}
    return render(request, 'new.html', data)


@login_required
def show(request, id):
    book = get_object_or_404(Books, pk=id)
  
    # data = {'book': book}
    # return render(request, 'show.html', data)

    if request.method == 'POST':
        form = AssignOwnerForm(request.POST)
        form2 = RemoveOwner(request.POST)
        
        if ("borrow" in request.POST):
            if form.is_valid():
                book.borrower = request.user
                book.save()
                return redirect("library-show", id=id)

        if ("return" in request.POST):
            if form2.is_valid():
                book.borrower = None
                book.save()
                return redirect("library-show", id=id)
    else:
        form = AssignOwnerForm(initial={'borrower': request.user})
        form2 = RemoveOwner(initial={'borrower': None})
        
    data = {
        'book': book,
        'form': form,
        'form2': form2
    }
    return render(request, "show.html", data)


def not_found_404(request, exception):
    data = {'err': exception}
    return render(request, '404.html', data)

def server_error_500(request):
    return render(request, '500.html')