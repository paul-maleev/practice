from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
from myLibrary import settings
from orders.models import *
from search.models import *
from django.conf.urls import patterns, url
from library.views import *

from django.contrib.auth.views import login, logout
from django.contrib.auth.forms import AuthenticationForm
from library.views import register

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^login/$', login),
                       url(r'^logout/$', logout),
                       url(r'^register/$', register),
                       url(r'^/$', BookListView.as_view())
                       url(r'^library/$', BookListView.as_view()),
                       url(r'^library/books/$', BookListView.as_view()),
                       url(r'^library/books/(?P<pk>\d+)/$',
                           BookCardView.as_view(), name='book_id'),
                       url(r'^library/authors/$', AuthorsListView.as_view()),
                       url(r'^library/authors/(?P<pk>\d+)/$',
                           AuthorCardView.as_view(), name='author_id'),
                       url(r'^upload/(?P<path>.*)$', 'django.views.static.serve', {
                           'document_root': settings.MEDIA_ROOT, }),
                       url(r'^orders.html', CustomersList.as_view()),
                       url(r'^customer.html/(?P<slug>[-_\w]+)/$',
                           CustomerDetails.as_view()),
                       url(r'^book_search.html', 'search.views.search'),
                       #                    url(r'^(?P<book_id>)/$', views.show, name='get_id'),




                       # Examples:
                       # url(r'^$', 'myLibrary.views.home', name='home'),
                       # url(r'^myLibrary/', include('myLibrary.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       )
