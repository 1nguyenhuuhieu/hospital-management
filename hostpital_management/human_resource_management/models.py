from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Staff(models.Model):
    user = models.OneToOneField(User, verbose_name='tài khoản đăng nhập', blank=True, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, verbose_name='Họ và tên')
    phone = models.IntegerField()
    detail = models.OneToOneField('StaffDetail', verbose_name='thông tin chi tiết', blank=True, null=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name  = 'nhân viên'
        verbose_name_plural  = 'nhân viên'

    def __str__(self):
        return self.full_name

class StaffDetail(models.Model):
    pass

