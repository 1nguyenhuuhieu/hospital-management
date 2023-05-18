from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget 
from news.models import *

class PostForm(forms.ModelForm):
    content = forms.CharField(label='Nội dung',widget=CKEditorUploadingWidget ())
    description = forms.CharField(label='Tóm tắt bài viết',widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model = Post
        fields = ['title', 'category', 'description', 'content']

