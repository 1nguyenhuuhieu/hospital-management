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

# tabular admin inline

class SelfAssessmentInline(admin.TabularInline):
    model = SelfAssessment

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
    fields = ['title']
    readonly_fields = ["title"]

    ordering = ('evaluation_criteria',)
    resource_classes = [EvaluationCriteriaResource]
    list_display = ('__str__','evaluation_criteria','title')
    list_filter = ('section_chapter__section', 'section_chapter__chapter', 'evaluation_criteria')

    inlines = [
        SelfAssessmentInline,
    ]


@admin.register(Level)
class LevelAdmin(ImportExportModelAdmin):
    resource_classes = [LevelResource]
    list_display = ('__str__', )

    list_filter = ('evaluation_criteria__section_chapter__section', 'evaluation_criteria__section_chapter__chapter', 'evaluation_criteria__evaluation_criteria', 'level')


@admin.register(Condition)
class ConditionAdmin(ImportExportModelAdmin):
    resource_classes = [ConditionResource]
    list_display = ('evaluation_criteria_level', 'title' )
    list_filter = ('evaluation_criteria_level__evaluation_criteria__section_chapter__section',
                   'evaluation_criteria_level__evaluation_criteria__section_chapter__chapter',
                   'evaluation_criteria_level__evaluation_criteria__evaluation_criteria',
                   'evaluation_criteria_level__level',
                   'index')
    
@admin.register(SelfAssessment)
class SelfAssessmentAdmin(admin.ModelAdmin):
    pass