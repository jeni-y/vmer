from django.contrib import admin

from .models import Sigup

@admin.register(Sigup)
class SiginAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_filter = ('username, ')
    search_fields = ('username',)