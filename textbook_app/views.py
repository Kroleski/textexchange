from .forms import BookForm, OwnedBookForm, UserForm
from .models import User, Book, OwnedBook
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

def index(request):
    available_books = OwnedBook.objects.filter(is_available=True).order_by('book__title')
    return render(request, 'textbook_app/index.html', {'available_books': available_books})

def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')  # Replace 'book_list' with the URL name for your book list view
    else:
        form = BookForm()
    return render(request, 'textbook_app/book_add.html', {'form': form})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'textbook_app/book_edit.html', {'form': form, 'book': book})

def book_confirm_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    return render(request, 'textbook_app/book_confirm_delete.html', {'book': book})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'textbook_app/book_list.html', {'books': books})

def owned_book_add(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = OwnedBookForm(request.POST)
        if form.is_valid():
            owned_book = form.save(commit=False)
            owned_book.user = user
            owned_book.save()
            return redirect('user-detail', pk=user.id)
    else:
        form = OwnedBookForm()
    return render(request, 'textbook_app/owned_book_add.html', {'form': form})

def toggle_availability(request, owned_book_id):
    owned_book = get_object_or_404(OwnedBook, id=owned_book_id)
    owned_book.is_available = not owned_book.is_available
    owned_book.save()
    return redirect('user-detail', pk=owned_book.user.id)

def user_add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = BookForm()
    return render(request, 'textbook_app/book_add.html', {'form': form})

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