from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.sites.models import RequestSite, Site
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render_to_response
from weblog.models import Entry, Weblog

# comment this out, to use a Generic view (see url's 'about' line)
#class AboutView(TemplateView):
#    template_name = "about.html"

class EntryListView(ListView):

    model = Entry

    template_name = "weblog/entry_list.html"
    
    def get_queryset(self):

        # TODO only get queryset relevant to subdomain (e.g. ciaron.example.com -> ciaron) 
        # or site (e.g. ciaronlinstead.com -> ciaron)
    
        if self.request.subdomain != None:
            site = get_object_or_404(User, username=self.request.subdomain)
            self.weblog = get_object_or_404(Weblog, author=site)
            return Entry.objects.filter(weblog=self.weblog)

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        #context['weblog_slug'] = self.weblog.slug
        return context

    def render_to_response(self, context):

        weblogs = Weblog.objects.all()

        if not self.request.subdomain:
            return render_to_response('weblog/weblog_list.html', {'object_list':weblogs})

        return super(EntryListView, self).render_to_response(context)

class EntryDetailView(DetailView):

    model = Entry

    # Can this filtering be done in a Model Manager instead?
    def get_object(self):
        siteowner = get_object_or_404(User, username=self.request.subdomain)
        entry = get_object_or_404(Entry, slug=self.kwargs['entry_slug'])

        if entry.weblog.author != siteowner:
            raise Http404
        else:
            return entry

