# bookproject/book/admin.py
from django.contrib import admin
from .models import Book, Review    # 追加



admin.site.register(Book)
admin.site.register(Review)         # 追加