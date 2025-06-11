from django.contrib import admin
from .models import PageView

@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'source', 'country', 'region', 'city', 'browser', 'operating_system', 'timestamp')
    search_fields = ('ip_address', 'source', 'country', 'referrer', 'browser', 'operating_system')
    list_filter = ('source', 'country', 'region', 'timestamp')