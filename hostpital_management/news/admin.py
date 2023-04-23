from django.contrib import admin
from .models import *
# Register your models here.


class TagInline(admin.StackedInline):
    model = Tag

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_show')
    fields = ('title', 'cover','image_tag', 'is_show','post', )
    readonly_fields = ('image_tag',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title',  'is_public', 'youtube_url')
    list_display_links = ('title', )
    list_filter = ('author', 'is_public',  'tags')
    filter_horizontal = ('tags',)
    readonly_fields = ('view_count', 'like')
    search_fields = ("title", 'author__name', 'tags__title',)

admin.site.register(Author)
admin.site.register(Comment)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    inlines = [TagInline, ]