# captcha/admin.py
from django.contrib import admin
from .models import CaptchaLog, PageView

@admin.register(CaptchaLog)
class CaptchaLogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'timestamp', 'action')

@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'source', 'country', 'city', 'browser', 'operating_system', 'timestamp')
    list_filter = ('source', 'country', 'browser', 'operating_system', 'timestamp')
    search_fields = ('ip_address', 'city', 'country')