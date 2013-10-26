#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

reload(sys)
sys.setdefaultencoding("utf-8")

__author__ = 'student'
from django.contrib import admin
from library.models import *


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email']
    list_display_links = ['last_name', 'first_name']
    ordering = ['last_name', 'first_name']


class ImageInline(generic.GenericTabularInline):
    model = BookImage
    extra = 0


class BooksAdmin(admin.ModelAdmin):
    def covers_count(self, obj):
        return BookImage.objects.filter(id=obj.id).count()

    list_display = ['title', 'publisher', 'publication_date', 'covers_count',]
    list_display_links = ['title']

    search_fields = ['title']
    date_hierarchy = 'publication_date'
    fieldsets = (
        (None, {'fields': ('title','authors','publication_date',)}),
        ('Выходные данные', {
            'classes': ('wide',),
            'description': 'Данные об издательстве',
            'fields': ('publisher',),
        }),
    )
    filter_horizontal = ('authors',)
    inlines = [ImageInline, ]


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['title', 'country', 'city']
    list_display_links = ['title']
    ordering = ['title']
    list_filter = ['country', 'city']
    fieldsets = (
        (None, {'fields': ('title',)}),
        ('Контактная информация', {
            'classes': ('wide',),
            'description': 'Контактная информация',
            'fields': ('country', 'city', 'address'),
        }),
    )


admin.site.register(Book, BooksAdmin)
admin.site.register(Author, AuthorsAdmin)
admin.site.register(Publisher, PublisherAdmin)


