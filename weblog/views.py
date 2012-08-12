from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.sites.models import RequestSite
from django.shortcuts import get_object_or_404
from weblog.models import Entry, Weblog

# comment this out, to use a Generic view (see url's 'about' line)
#class AboutView(TemplateView):
#    template_name = "about.html"

class EntryListView(ListView):

    model = Entry
    
    def get_queryset(self):
        self.weblog = get_object_or_404(Weblog, slug=self.kwargs['weblog_slug'])
        return Entry.objects.filter(weblog=self.weblog)
    
    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['weblog_slug'] = self.weblog.slug
        return context

class EntryDetailView(DetailView):

    model = Entry

    def get_object(self):
        return get_object_or_404(Entry, slug=self.kwargs['entry_slug'])
