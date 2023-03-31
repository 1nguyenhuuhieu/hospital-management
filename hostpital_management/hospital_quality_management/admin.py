from django.contrib import admin
from .models import *
# Register your models here.
# tabular inline admin

class RequestLevelInline(admin.TabularInline):
    model = RequestLevel

    
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('index', 'title')
    list_display_links = ('title',)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('pre_index','index', 'title')
    list_display_links = ('title',)
    list_filter = ('pre_index', 'index')
    ordering = ['pre_index','index']
    search_fields = ['pre_index__index','index','title']

@admin.register(EvaluationCriteria)
class EvaluationCriteriaAdmin(admin.ModelAdmin):
    list_display = ('pre_index','index', 'title')
    list_display_links = ('title',)
    inlines = [
        RequestLevelInline,
    ]

admin.site.register(File)
admin.site.register(RequestLevel)
