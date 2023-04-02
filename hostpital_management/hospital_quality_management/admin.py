from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

from import_export import resources
# Register your models here.
# tabular inline admin

class LevelInline(admin.TabularInline):
    model = Level

class ResponserInline(admin.TabularInline):
    model = Responser

class LevelResource(resources.ModelResource):

    class Meta:
        model = Level
        fields = ('id','pre_index','level',)

class SectionResource(resources.ModelResource):

    class Meta:
        model = Section
        fields = ('id', 'index', 'title',)

class ChapterResource(resources.ModelResource):

    class Meta:
        model = Chapter
        fields = ('id', 'pre_index','index', 'title',)

class EvaluationCriteriaResource(resources.ModelResource):

    class Meta:
        model = EvaluationCriteria
        fields = ('id', 'pre_index','index', 'title',)

class ConditionResource(resources.ModelResource):

    class Meta:
        model = Condition
        fields = ('id','pre_index','index','title',)

@admin.register(Section)
class SectionAdmin(ImportExportModelAdmin):
    list_display = ('index', 'title')
    list_display_links = ('title',)
    resource_classes = [SectionResource]

@admin.register(Chapter)
class ChapterAdmin(ImportExportModelAdmin):
    list_display = ('pre_index','index', 'title')
    list_display_links = ('title',)
    list_filter = ('pre_index', 'index')
    ordering = ['pre_index','index']
    search_fields = ['pre_index__index','index','title']
    resource_classes = [ChapterResource]


@admin.register(EvaluationCriteria)
class EvaluationCriteriaAdmin(ImportExportModelAdmin):
    list_display = ('index_name', 'title')
    ordering = ['pre_index','index']
    list_filter = ('pre_index__pre_index__index','pre_index__index', 'index')

    list_display_links = ('title',)
    inlines = [
        LevelInline,
        ResponserInline
    ]
    resource_classes = [EvaluationCriteriaResource]


@admin.register(Condition)
class ConditionAdmin(ImportExportModelAdmin):
    resource_classes = [ConditionResource]
class RequestLevelAdmin(ImportExportModelAdmin):
    resource_classes = [LevelResource]

admin.site.register(File)
admin.site.register(Level, RequestLevelAdmin)
admin.site.register(Responser)
