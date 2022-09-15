from django.shortcuts import render, redirect
from .models import ListedBook
from .forms import BookForm

# Create your views here.


def home(request):
    return render(request, 'store/home.html')


def get_books(request):
    # TODO: get all books from the database
    books = ListedBook.objects.all()
    return render(request, 'store/books.html', {'books': books})


def get_book(request, book_id: int):
    # get a specific book by id
    book = ListedBook.objects.get(id=book_id)
    return render(request, 'store/book.html', {'book': book})


def add_book(request):
    if (request.method == 'POST'):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store:get_books')
    else:
        form = BookForm()
    return render(request, 'store/add_book.html', {'form': form})


def edit_book(request, book_id: int):
    if (request.method == 'POST'):
        book = ListedBook.objects.get(id=book_id)
        form = BookForm(request.POST, instance=book, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store:get_books')
    else:
        book = ListedBook.objects.get(id=book_id)
        form = BookForm(instance=book)
    return render(request, 'store/edit_book.html', {'form': form})


def delete_book(request, book_id: int):
    book = ListedBook.objects.get(id=book_id)
    book.delete()
    return redirect('store:get_books')
