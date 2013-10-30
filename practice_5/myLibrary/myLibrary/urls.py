from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
from myLibrary import settings
from myLibrary.settings import MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'library.views.index'),
                       url(r'^library/$', 'library.views.index'),
                       url(r'^library/books/$', 'library.views.index'),
                       url(r'^library/books/(\d+)/$',
                           'library.views.bookCard'),
                       url(r'^library/authors/$', 'library.views.authors'),
                       url(r'^library/authors/(\d+)/$',
                           'library.views.authorsCard'),
                       url(r'^upload/(?P<path>.*)$', 'django.views.static.serve', {
                           'document_root': settings.MEDIA_ROOT, }),

                       # Examples:
                       # url(r'^$', 'myLibrary.views.home', name='home'),
                       # url(r'^myLibrary/', include('myLibrary.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       )
