from django.contrib import admin
from bs4 import BeautifulSoup
from unidecode import unidecode




from .models import *
# Register your models here.


class TagInline(admin.StackedInline):
    model = Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    exclude = ('user','plaintext_content','view_count','like')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        # remove HTML tags from richtext field
        plain_text = BeautifulSoup(obj.content).get_text()
        # lower string
        plain_text = plain_text.lower()
        # convert tiếng việt có dấu sang không dấu
        plain_text = unidecode(plain_text)

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