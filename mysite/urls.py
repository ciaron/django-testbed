from django.conf.urls import patterns, include, url
#from weblog.views import AboutView
from django.views.generic import TemplateView, ListView, DetailView
from weblog.models import Entry, Weblog
from weblog.views import EntryDetailView, EntryListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    #(r'^about/', AboutView.as_view()),
    url(r'^$', ListView.as_view(model=Weblog,)),
    (r'^about/', TemplateView.as_view(template_name="about.html")),

    # TODO: filter entries according to weblog
    # i.e. change URL to r'^(?P<weblog-slug>[-\w]+)/$')
    #(r'^entries/$', ListView.as_view(model=Entry,)), # template name is inferred as 'entry_list.html'
    (r'^(?P<weblog_slug>[-\w]+)/$', EntryListView.as_view()), # show entries for <weblog>, template name is inferred as 'entry_list.html'

    url(r'^entry/(?P<pk>\d+)/$', DetailView.as_view(model=Entry,),
        #EntryDetailView.as_view(),
        name='entry-detail',
    ),

    url(r'^entry/(?P<slug>[-\w]+)/$',
        DetailView.as_view(model=Entry,),
        name='entry-detail',
    ),

    # want to show entry_list, filtered for <slug>-blog
    #url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(model=Weblog,), name='weblog-detail',),

)
