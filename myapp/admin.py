from django.contrib import admin
from .models import Name

@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ('name','published_date')
