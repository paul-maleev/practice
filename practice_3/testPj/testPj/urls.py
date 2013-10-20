from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'lister.views.index'),
                       url(r'^log/(?P<file_path>.*)$', 'lister.views.listing'),
                       # Examples:
                       # url(r'^$', 'testPj.views.home', name='home'),
                       # url(r'^testPj/', include('testPj.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
)
