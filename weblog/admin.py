from weblog.models import Entry, Weblog
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class WeblogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Entry, EntryAdmin)
admin.site.register(Weblog, WeblogAdmin)

