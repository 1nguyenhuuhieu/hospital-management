from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import PIL.Image
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.html import mark_safe
import os


class Slide(models.Model):
    title = models.CharField(max_length=200, verbose_name='tiêu đề', default='banner')
    cover = models.ImageField(upload_to='slides/',verbose_name='ảnh slide', help_text='ảnh slide nên có tỉ lệ cao:rộng là 1:4 để đẹp nhất ')
    is_show = models.BooleanField(verbose_name='hiển thị trang chủ', default=True)
    post = models.ForeignKey('Post', blank=True, null=True, verbose_name='bài viết liên kết', on_delete=models.CASCADE)
    created_time = models.TimeField(auto_now_add=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.title = f'banner-{self.id}'
        super(Slide, self).save(*args, **kwargs)
        if self.cover:
            img = PIL.Image.open(self.cover)
            target_width = 1920
            target_height = target_width/4
            img = img.resize((int(target_width), int(target_height)), PIL.Image.ANTIALIAS)
            img.save(self.cover.path, quality=100)
            img.close()
            self.cover.close()


    def image_tag(self):
        return mark_safe('<img src="%s" height=100' % (self.cover.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'slide trang chủ'
        verbose_name_plural = 'slide trang chủ'
    def __str__(self):
        return f'{self.title}'
    
class Tag(models.Model):
    title = models.CharField(max_length=200, verbose_name='tên đầy đủ')
    parrent_tag = models.ForeignKey('self', verbose_name='danh mục cha', blank=True, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name = 'danh mục'
        verbose_name_plural = 'danh mục'

    def __str__(self):
        return f'{self.title}'
    
class Post(models.Model):
    title = models.CharField(max_length=1000, verbose_name='tên bài viết')
    author = models.ForeignKey('Author', verbose_name='tác giả', blank=True, null=True, on_delete=models.CASCADE)
    is_public = models.BooleanField(verbose_name='có hiển thị bài viết', default=True)
    content = RichTextUploadingField(verbose_name='nội dung')
    youtube_url = models.URLField(max_length=40, blank=True, null=True, verbose_name='URL video youtube', help_text='dán url video youtube vào đây')
    cover = models.ImageField(upload_to='post-covers/', verbose_name='ảnh bìa', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='danh mục', blank=True)
    created_time = models.DateTimeField(auto_now_add=True,null=True)
    updated_time = models.DateTimeField(auto_now=True,null=True)
    view_count = models.IntegerField(blank=True, null=True, default=0, verbose_name='số lượt xem')
    like = models.IntegerField(blank=True, null=True, default=0, verbose_name='số lượt like')

    def youtube_id(self):
        if self.youtube_url:
            youtube_url = self.youtube_url
            str1_s = youtube_url.split('/')
            str1_s = str1_s[3].split('?')
            return str1_s[0]
        else:
            return None
        
    def tags_list(self):
        return '; '.join(tag.title for tag in self.tags.all())
    def tags_list_id(self):
        return list(tag.id for tag in self.tags.all())
    class Meta:
        verbose_name = 'bài viết'
        verbose_name_plural = 'bài viết'

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    author = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
        verbose_name = 'bình luận'
        verbose_name_plural = 'bình luận'

    def __str__(self):
        return f'{self.comment}' 

class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='tên')
    description = models.CharField(max_length=200, verbose_name='mô tả ngắn')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='ảnh đại diện', blank=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            img = PIL.Image.open(self.avatar)
            img = img.resize((200, 200), PIL.Image.ANTIALIAS)
            img.save(self.avatar.path, quality=100)
            img.close()
            self.avatar.close()


    class Meta:
        verbose_name = 'tác giả'
        verbose_name_plural = 'tác giả'

    def __str__(self):
        return f'{self.name}' 
