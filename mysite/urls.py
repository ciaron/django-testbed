from django.conf.urls import patterns, include, url
#from weblog.views import AboutView
from django.views.generic import TemplateView, ListView, DetailView
from weblog.models import Entry
from weblog.views import EntryDetailView

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
    (r'^about/', TemplateView.as_view(template_name="about.html")),

    (r'^entries/$', ListView.as_view(model=Entry,)), # template name is inferred as 'entry_list.html'

#    (r'^entry/(?P<pk>\d+)/$',
    url(r'^entry/(?P<pk>\d+)/$',
        #DetailView.as_view(model=Entry,),
        EntryDetailView.as_view(),
        name='entry-detail',
    ),

)
