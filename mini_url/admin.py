from django.contrib import admin

# Register your models here.
from mini_url.models import Raccourci

class RaccourciAdmin(admin.ModelAdmin):
    list_display   = ('URLField', 'code', 'date', 'pseudo', 'nb_acces')
    list_filter    = ('pseudo',)
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('URLField',)
    fields = ('URLField', 'code', 'date', 'pseudo')
 
admin.site.register(Raccourci, RaccourciAdmin)
