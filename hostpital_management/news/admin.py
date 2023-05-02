from django.contrib import admin
from bs4 import BeautifulSoup




from .models import *
# Register your models here.


class TagInline(admin.StackedInline):
    model = Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    readonly_fields = ('view_count', 'like')
    exclude = ('user',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        plain_text = BeautifulSoup(obj.content).get_text()
        obj.plaintext_content = plain_text
        
        super().save_model(request, obj, form, change)

admin.site.register(Author)
admin.site.register(Comment)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass