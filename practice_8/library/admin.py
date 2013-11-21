#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

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
        counter = 0
        for c in BookImage.objects.filter(id=obj.id):
            if c.small_image:
                counter += 1
            if c.large_image:
                counter += 1
        return counter
    covers_count.allow_tags = True

    def get_img_cover(self, obj):
        link = ""
        for c in BookImage.objects.filter(id=obj.id):
            link = c.img_tag()
        return link
    get_img_cover.allow_tags = True

    def get_large_img_cover(self, obj):
        link = ""
        for c in BookImage.objects.filter(id=obj.id):
            link = c.img_tag()
        return link
    get_large_img_cover.allow_tags = True

    list_display = ['title', 'isbn', 'publisher', 'publication_date',
                    'covers_count', 'get_img_cover', 'get_large_img_cover', ]
    list_display_links = ['title']

    search_fields = ['title']
    date_hierarchy = 'publication_date'
    fieldsets = (
        (None, {'fields': ('title', 'isbn', 'authors', 'publication_date', 'description',)}),
        ('Выходные данные', {
            'classes': ('wide',),
            'description': 'Данные об издательстве',
            'fields': ('publisher',),
        }),
    )
    filter_horizontal = ('authors',)
    inlines = [ImageInline, ]


class BookImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_cover', 'img_tag', 'large_img_tag']


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['title', 'country', 'city', ]
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
# admin.site.register(BookImage,BookImageAdmin)
admin.site.register(Author, AuthorsAdmin)
admin.site.register(Publisher, PublisherAdmin)
