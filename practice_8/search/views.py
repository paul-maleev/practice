# Create your views here.
#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import *
from django.db import connection
from django.shortcuts import render_to_response, render
from search.models import *
from library.models import Book
from django.shortcuts import get_object_or_404, render_to_response

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def search(request):
    books = Book.objects.all()
    books = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            book_title = form.cleaned_data['book_title']
            form_isbn = form.cleaned_data['ISBN']
            if book_title:
                books = Book.objects.filter(title=book_title)
            elif form_isbn:
                books = Book.objects.filter(isbn=form_isbn)
            form.save()
    else:
        form = SearchForm()
    return render(request, "book_search.html", {'form': form, 'books': books})
