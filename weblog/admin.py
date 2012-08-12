from weblog.models import Entry, Weblog, UserProfile
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class WeblogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class UserProfileAdmin(admin.ModelAdmin):
    #prepopulated_fields = {"slug": ("title",)}
    pass

admin.site.register(Entry, EntryAdmin)
admin.site.register(Weblog, WeblogAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

