#!/usr/bin/python
# -*- coding: utf-8 -*- 

from django.http import HttpResponse, Http404
from django.db import connection
from library.models import Book, Author
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# Create your views here.

def index(request):
	html = "<center><p>Список книг:</p></center>\n"
	html+="<table border=1>"
	for e in Book.objects.all():
		authors=""
		for a in e.authors.all():
			authors+=" "+a.__unicode__()
		html+="<tr><td><a href=\""+e.get_absolute_url()+"\">"+e.title+"</a></td><td>"+authors+"</td><td>"+e.publisher.__unicode__()+"</td></tr>"
	html+="</table>"
	return HttpResponse(html)

def books(request,id):
	html="<center><p>Информация о книге</p>"
	book = Book.objects.raw("SELECT * FROM library_book WHERE id = %s",[id])[0]
	html+="<table border=1>"
	html+="<tr><td>Название книги:</td><td>"+book.__unicode__()+"</td></tr>"
	IDs = connection.cursor()
	IDs = IDs.execute("SELECT A.id FROM library_author AS A JOIN library_book_authors AS B ON A.id=B.id WHERE B.book_id = %s",[id])
	authors=""
	for i,a in zip(IDs.fetchall(),book.authors.all()):
		authors+="<a href=\"/library/authors/"+str(i[0])+"/\">"+a.__unicode__()+"</a>,  "

	html+="<tr><td>Автор(ы): </td><td>"+authors+"</td></tr>"
	html+="<tr><td>Издатель: </td><td>"+book.publisher.__unicode__()+"</td></tr>"
	html+="<tr><td>Дата выхода:</td><td>"+str(book.publication_date)+"</td></tr></table></center>"
	return HttpResponse(html)

def authors(request):
	html="<p>Список авторов</p>"
	html+="<table border=1>"
	for a in Author.objects.all():
		authorId = connection.cursor()
		authorId = authorId.execute("SELECT id FROM library_author WHERE first_name=%s AND last_name=%s",[a.first_name, a.last_name])
		ID = authorId.fetchall()[0][0]
		html+="<tr><td><a href=\"/library/authors/"+str(ID)+"/\">"+a.first_name+" "+a.last_name+"</a></td></tr>"
	html+="</table>"
	return HttpResponse(html)

def authorsId(request,id):
	html="<p>Карточка автора: </p>"
	author = Author.objects.raw("SELECT * FROM library_author WHERE id = %s",[id])[0]
	html+="<table border=1>"
	html+="<tr><td>Имя:	"+author.first_name+"</td></tr>"
	html+="<tr><td>Фамилия:	"+author.last_name+"</td></tr>"
	if author.email!=None:
		html+="<tr><td>E-mail:	"+author.email+"</td></tr>"
	html+="</table>"
	return HttpResponse(html)
	

