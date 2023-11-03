from .forms import BookForm
from .models import User, Book, OwnedBook
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

def index(request):
    available_books = OwnedBook.objects.filter(is_available=True).order_by('book__title')
    return render(request, 'textbook_app/index.html', {'available_books': available_books})

class UserListView(generic.ListView):
    model = User
    
class UserDetailView(generic.DetailView):
    model = User
    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user = self.get_object()
        owned_books = OwnedBook.objects.filter(user=user)
        context['owned_books'] = owned_books
        return context

class OwnedBookListView(generic.ListView):
    model = OwnedBook

class OwnedBookDetailView(generic.DetailView):
    model = OwnedBook
    def get_context_data(self, **kwargs):
        context = super(OwnedBookDetailView, self).get_context_data(**kwargs)
        ownedbook = self.get_object()
        context['ownedbook'] = Book.objects.filter(ownedbook=ownedbook)
        return context
    
class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

def addBook(request, ownedbook_id):
    ownedbook = OwnedBook.objects.get(pk=ownedbook_id)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.ownedbook = ownedbook
            book.save()
            return redirect('ownedbook-detail', ownedbook_id)
    else:
        form = BookForm()
        context = {'form': form}
        return render(request, 'textbook_app/book_form.html', context)