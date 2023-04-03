from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

from import_export import resources
# Register your models here.

# Khai báo cho module import-export django


class SectionResource(resources.ModelResource):
    class Meta:
        model = Section
        fields = ('id', 'section', 'title',)


class ChapterResource(resources.ModelResource):
    class Meta:
        model = Chapter
        fields = ('id', 'section', 'chapter', 'title',)


class EvaluationCriteriaResource(resources.ModelResource):
    class Meta:
        model = EvaluationCriteria
        fields = ('id', 'section_chapter', 'evaluation_criteria', 'title',)


class LevelResource(resources.ModelResource):
    class Meta:
        model = Level
        fields = ('id', 'evaluation_criteria', 'level',)


class ConditionResource(resources.ModelResource):
    class Meta:
        model = Condition
        fields = ('id', 'evaluation_criteria_level', 'index', 'title',)


# Khai báo trang admin models
@admin.register(Section)
class SectionAdmin(ImportExportModelAdmin):
    resource_classes = [SectionResource]
    list_display = ('section', 'title')


@admin.register(Chapter)
class ChapterAdmin(ImportExportModelAdmin):
    resource_classes = [ChapterResource]
    list_display = ('__str__','title')


@admin.register(EvaluationCriteria)
class EvaluationCriteriaAdmin(ImportExportModelAdmin):
    resource_classes = [EvaluationCriteriaResource]
    list_display = ('__str__','title')
    list_filter = ('section_chapter__section', 'section_chapter__chapter', 'evaluation_criteria')
@admin.register(Level)
class LevelAdmin(ImportExportModelAdmin):
    resource_classes = [LevelResource]


@admin.register(Condition)
class ConditionAdmin(ImportExportModelAdmin):
    resource_classes = [ConditionResource]
