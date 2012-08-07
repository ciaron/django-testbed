from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.sites.models import RequestSite
from django.shortcuts import get_object_or_404
from weblog.models import Entry, Weblog

# comment this out, to use a Generic view (see url's 'about' line)
#class AboutView(TemplateView):
#    template_name = "about.html"

class EntryListView(ListView):

    model = Entry
    template_name='entry_list.html'
    
    def get_queryset(self):
#        raise Exception
        print self.kwargs
        self.weblog = get_object_or_404(Weblog, slug=self.kwargs['weblog_slug'])
        return Entry.objects.filter(weblog=self.weblog)
    
class EntryDetailView(DetailView):
    model = Entry

    def get_context_data(self, **kwargs):

        #site_name = request.get_host()
        #site = RequestSite(self.request)
        #print "site.domain: %s" % site.domain
        #print "site.name: %s" % site.name

        context = super(EntryDetailView, self).get_context_data(**kwargs)
        #context['dahl_books'] = Books.objects.filter(author="Dahl")
        return context
