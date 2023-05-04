from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import PIL.Image
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from human_resource_management.models import *
from django.utils import timezone
import os

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='tên danh mục')
    cover = models.ImageField(upload_to='tag-covers/', verbose_name='ảnh bìa', blank=True, null=True, help_text='ảnh bìa sẽ tự động resize về kích thước 768 x 432')


    class Meta:
        verbose_name = 'danh mục'
        verbose_name_plural = 'danh mục'

    def __str__(self):
        return f'{self.title}'
     
class Tag(models.Model):
    title = models.CharField(max_length=200, verbose_name='tên đầy đủ')
    cover = models.ImageField(upload_to='tag-covers/', verbose_name='ảnh bìa', blank=True, null=True, help_text='ảnh bìa sẽ tự động resize về kích thước 768 x 432')

    class Meta:
        verbose_name = 'thẻ'
        verbose_name_plural = 'thẻ'

    def __str__(self):
        return f'{self.title}'
    
class Post(models.Model):
    title = models.CharField(max_length=1000, verbose_name='tên bài viết')
    category = models.ForeignKey(Category, verbose_name='danh mục', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey('Author', verbose_name='tác giả', blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='người đăng', blank=True, null=True, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('private', 'Chỉ mình tôi'),
        ('staff', 'Nhân viên'),
        ('public', 'Mọi người')
    ]
    status = models.CharField(choices=STATUS_CHOICES,verbose_name='trạng thái bài viết', default='public', max_length=10)
    description = models.TextField(verbose_name='tóm tắt')
    content = RichTextUploadingField(verbose_name='nội dung')
    plaintext_content = models.TextField(verbose_name='plain text of content', blank=True, null=True)
    youtube_url = models.URLField(max_length=40, blank=True, null=True, verbose_name='URL video youtube', help_text='dán url video youtube vào đây')
    cover = models.ImageField(upload_to='post-covers/', verbose_name='ảnh bìa', blank=True, null=True, help_text='ảnh bìa sẽ tự động resize về kích thước 768 x 432')
    tags = models.ManyToManyField(Tag, verbose_name='thẻ', blank=True)
    created_time = models.DateTimeField(auto_now_add=True,null=True)
    updated_time = models.DateTimeField(auto_now=True,null=True)
    view_count = models.IntegerField(blank=True, null=True, default=0, verbose_name='số lượt xem')
    like = models.IntegerField(blank=True, null=True, default=0, verbose_name='số lượt like')

    def get_cover_image(self):
        if self.cover:
            return self.cover.url
        else:
            if self.tags:
                for tag in self.tags.all():
                    if tag.cover:
                        return tag.cover.url
            if self.category.cover:
                return self.category.cover.url
            else:
                return 'static/imgs/no-image.png'

    
    def status_icon(self):
        if self.status == 'public':
            return 'globe-americas'
        else:
            return 'people'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.cover:
            img = PIL.Image.open(self.cover)
            width, height = img.size
            img_ratio = width/height
            target_width = 768
            target_height = 432
            ratio = target_width/target_height
            
            if ratio > img_ratio:
                ratio_width = target_width
                ratio_height = ratio_width / img_ratio
            elif ratio < img_ratio:
                ratio_height = target_height
                ratio_width = ratio_height * img_ratio
            else:
                ratio_width = target_width
                ratio_height = target_height

            img = img.resize((round(ratio_width), round(ratio_height)), PIL.Image.ANTIALIAS)
            width, height = img.size

            if width > target_width:
                delta = width - target_width
                top = 0
                bot = height
                left = delta/2
                right = width - left
            
            elif height > target_height:
                delta = height - target_height
                left = 0
                right = width
                delta = height - target_height
                top = delta/2
                bot = height-top
            
            else:
                top = 0
                bot = height
                left = 0
                right = width

            img = img.crop((left, top, right, bot))
            img.save(self.cover.path, quality=100)
            img.close()
            self.cover.close()

    def youtube_id(self):
        if self.youtube_url:
            youtube_url = self.youtube_url
            str1_s = youtube_url.split('/')
            str1_s = str1_s[3].split('?')
            return str1_s[0]
        else:
            return None
        
    def is_old_created_time(self):
        now = timezone.now()
        date_diff = (now - self.created_time).days

        return date_diff > 0
        
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
    cover = models.ImageField(upload_to='covers/', verbose_name='ảnh bìa', blank=True)

    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return 'static/imgs/no-image.png'


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