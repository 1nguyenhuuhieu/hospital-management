from django.db import models
from django.contrib.auth.models import User
import PIL.Image


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='tài khoản đăng nhập', blank=True, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, verbose_name='Họ và tên')
    phone = models.IntegerField(blank=True, null=True)

    avatar = models.ImageField(upload_to='avatars/', verbose_name='ảnh đại diện', blank=True, null=True)

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
        verbose_name  = 'thành viên'
        verbose_name_plural  = 'thành viên'

    def __str__(self):
        return self.full_name