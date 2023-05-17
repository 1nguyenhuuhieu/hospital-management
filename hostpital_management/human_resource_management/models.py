from django.db import models
from django.contrib.auth.models import User
import PIL.Image



# Create your models here.
class Staff(models.Model):
    user = models.OneToOneField(User, verbose_name='tài khoản đăng nhập', blank=True, null=True, on_delete=models.CASCADE)
    SEX_CHOICES = [
        ("m", "Nam"),
        ('f', "Nữ")
    ]

    full_name = models.CharField(max_length=200, verbose_name='Họ và tên')
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    department = models.ForeignKey("Department", blank=True, null=True, verbose_name="Khoa/Phòng", on_delete=models.CASCADE)
    is_work = models.BooleanField(verbose_name="trạng thái làm việc", default=True)
    birth_date = models.DateField( verbose_name='ngày sinh', blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True, verbose_name='giới tính')
    address = models.CharField(max_length=1000, blank=True, null=True, verbose_name='địa chỉ hiện tại')

    class Meta:
        verbose_name  = 'nhân viên'
        verbose_name_plural  = 'nhân viên'

    def __str__(self):
        return self.full_name

class Department(models.Model):
    pass

