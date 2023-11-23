from django.contrib import admin
from .models import User, Book, OwnedBook

admin.site.register(User)
admin.site.register(Book)
admin.site.register(OwnedBook)