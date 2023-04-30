from django.contrib import admin
from .models import *
# Register your models here.


class TagInline(admin.StackedInline):
    model = Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    readonly_fields = ('view_count', 'like')

admin.site.register(Author)
admin.site.register(Comment)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass