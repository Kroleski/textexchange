from .forms import BookForm
from .models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic
from typing import Any

def index(request):

# Render the HTML template index.html with the data in the context variable.
   return render( request, 'textbook_app/index.html')

class UserListView(generic.ListView):
    model = User
    
class UserDetailView(generic.DetailView):
    model = User