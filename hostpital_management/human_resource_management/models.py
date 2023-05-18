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
        return f'{self.full_name} {self.birth_date}'

class Department(models.Model):
    pass

class Team(models.Model):
    title = models.CharField(max_length=200, verbose_name='tên nhóm')
    created_date = models.DateField(auto_now_add=True, verbose_name='thời gian tạo')
    class Meta:
        verbose_name  = 'nhóm'
        verbose_name_plural  = 'nhóm'

    def __str__(self):
        return self.title

class StaffTeam(models.Model):
    ROLE_CHOICES = [
        (0, 'Thành viên'),
        (1, 'Trưởng nhóm'),
        (2, 'Phó nhóm'),
    ]
    staff = models.ForeignKey(Staff, verbose_name='nhân viên', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, verbose_name='nhóm', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True, verbose_name='thời gian tạo')
    role = models.IntegerField(choices=ROLE_CHOICES, default=0, verbose_name='vị trí')


    class Meta:
        verbose_name  = 'thành viên nhóm'
        verbose_name_plural  = 'thành viên nhóm'
        unique_together = ['staff','team']

    def __str__(self):
        return f'{self.staff}, {self.team}'

  


