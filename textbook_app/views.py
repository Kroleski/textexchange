import requests
from .forms import BookForm, BookSearchForm, OwnedBookForm, UserForm
from .models import User, Book, OwnedBook
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

def index(request):
    available_books = OwnedBook.objects.filter(is_available=True).order_by('book__title')
    return render(request, 'textbook_app/index.html', {'available_books': available_books})

# @login_required
# def book_add(request):
#     book_info = request.session.pop('book_info', None)
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             book = form.save(commit=False)
#             if book_info:
#                 form = BookForm({
#                     'isbn': book_info['isbn'],
#                     'title': book_info['title'],
#                     'author': book_info['author'],
#                     'description': book_info['description'],
#                 })
#             book.ownedbook = ownedbook
#             book.save()
#             messages.success(request, 'Book added successfully!')
#             return redirect('ownedbook-detail', ownedbook_id)
#     else:
#         form = BookForm()
#     return render(request, 'textbook_app/book_add.html', {'form': form})

@login_required
def book_add(request):
    book_info = request.session.pop('book_info', None)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            if book_info:
                book.isbn = book_info['isbn']
                book.title = book_info['title']
                book.author = book_info['author']
                book.description = book_info['description']
            book.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'textbook_app/book_add.html', {'form': form})
def book_added_success(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'textbook_app/book_added_success.html', {'book': book})

@login_required
def book_search_google(request):
    if request.method == 'POST':
        search_form = BookSearchForm(request.POST)
        if search_form.is_valid():
            isbn = search_form.cleaned_data['isbn']
            api_url = f'https://www.googleapis.com/books/v1/volumes?q={isbn}'
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                book_info = data.get('items', [])[0].get('volumeInfo', {})
                book, created = Book.objects.update_or_create(
                    isbn=isbn,
                    defaults={
                        'title': book_info.get('title', ''),
                        'author': ', '.join(book_info.get('authors', [])),
                        'description': book_info.get('description', ''),
                    }
                )
                if created:
                    messages.success(request, 'Book added successfully!')
                else:
                    messages.info(request, 'Book already exists in the database.')
                return redirect('books')
    else:
        search_form = BookSearchForm()
    return render(request, 'textbook_app/book_search_google.html', {'search_form': search_form})

@login_required
def book_confirm_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    return render(request, 'textbook_app/book_confirm_delete.html', {'book': book})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'textbook_app/book_list.html', {'books': books})

@login_required
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

@login_required
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

@login_required
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
    return render(request, 'textbook_app/user_add.html', {'form': form})

class UserListView(LoginRequiredMixin, generic.ListView):
    model =User
    
class UserDetailView(LoginRequiredMixin, generic.DetailView):
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