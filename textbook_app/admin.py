from django.contrib import admin
from .models import User, Book, OwnedBook, BorrowedBook, WantedBook

admin.site.register(User)
admin.site.register(Book)
admin.site.register(OwnedBook)
admin.site.register(BorrowedBook)
admin.site.register(WantedBook)

