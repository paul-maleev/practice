from django.db import models, connection
from django.contrib import admin
from django.http import response
from library.models import Book
from utils.models import TimeStampedModel
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.template import RequestContext
from django import forms


class SearchForm(forms.Form):
    book_title = forms.CharField(max_length=128, required=False)
    ISBN = forms.CharField(max_length=18, required=False)

    def save(self):
        data = self.cleaned_data
