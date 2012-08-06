from django.views.generic import TemplateView, DetailView
from django.contrib.sites.models import RequestSite
from weblog.models import Entry

# comment this out, to use a Generic view (see url's 'about' line)
#class AboutView(TemplateView):
#    template_name = "about.html"

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
