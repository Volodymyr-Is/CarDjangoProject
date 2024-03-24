from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from books_app.models import Book
from django.shortcuts import render, get_object_or_404
from books_app.forms import BookForms
from django.views.decorators.csrf import csrf_exempt


def Books(request):
    if request.method == 'POST':
        form = BookForms(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=True)
            return HttpResponseRedirect(f'/books/{book.id}')
    books = Book.objects.all()
    return render(request, 'allBooks.html', {'book_list': books, 'form': BookForms()})


def getBook(request, book_id):
    my_book = get_object_or_404(Book, pk=book_id)   
    if request.method == 'POST':
        form = BookForms(request.POST, request.FILES, instance=my_book)
        form.save()
        return render(request, 'book.html', {'book': my_book, 'form': form})
    
    return render(request, 'book.html', {'book': my_book, 'form': BookForms(None, instance=my_book)})

def getBookByName(request, book_title):
    if request.method == 'GET':
        try:
            book = Book.objects.get(title__icontains=book_title)
            # return HttpResponseRedirect(f'/{book.pk}')
            return render(request, 'book.html', {'book': book})           
        except Book.DoesNotExist:
            return render(request, 'allBooks.html')         
    return render(request, 'allBooks.html')
    # return HttpResponseRedirect(f'/{book.id}/')
    # return render(request, 'book.html', {'book': book})


@csrf_exempt
def deleteBook(request, book_id):
    my_book = get_object_or_404(Book, pk=book_id)   
    if request.method == 'POST':
        my_book.delete()
        return HttpResponseRedirect('/allBooks')
    return render(request, 'allBooks.html', {'book_list': my_book})


def Home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'book_list': books})