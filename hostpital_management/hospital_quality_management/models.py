from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

from human_resource_management.models import *


# Models for Hospital Quality Management - HQM

# Phần tiêu chí đánh giá
class Section(models.Model):
    SECTION_CHOICES = (
        ('A', 'Phần A'),
        ('B', 'Phần B'),
        ('C', 'Phần C'),
        ('D', 'Phần D'),
        ('E', 'Phần E')
    )
    section = models.CharField('phần', max_length=1, choices=SECTION_CHOICES)
    title = models.TextField('tiêu đề')

    class Meta:
        verbose_name  = 'phần'
        verbose_name_plural  = 'phần'

    def __str__(self):
        return f'{self.section}'

# Chương tiêu chí đánh giá
class Chapter(models.Model):
    CHAPTER_CHOICES = (
        (1, 'Chương 1'),
        (2, 'Chương 2'),
        (3, 'Chương 3'),
        (4, 'Chương 4'),
        (5, 'Chương 5'),
        (6, 'Chương 6'),
        (7, 'Chương 7'),
        (8, 'Chương 8'),
        (9, 'Chương 9'),
        (10, 'Chương 10'),
    )
    section = models.ForeignKey(Section, verbose_name='phần', on_delete=models.CASCADE)
    chapter = models.IntegerField('chương', choices=CHAPTER_CHOICES)
    title = models.TextField('tiêu đề')
    
    class Meta:
        verbose_name  = 'chương'
        verbose_name_plural  = 'chương'

    def __str__(self):
        return f'{self.section}{self.chapter}'

# Tiêu chí đánh giá
class EvaluationCriteria(models.Model):
    ITEM_CHOICES = (
        (1, 'Mục 1'),
        (2, 'Mục 2'),
        (3, 'Mục 3'),
        (4, 'Mục 4'),
        (5, 'Mục 5'),
        (6, 'Mục 6'),
    )
    section_chapter = models.ForeignKey(Chapter, verbose_name='phần, chương', on_delete=models.CASCADE)
    evaluation_criteria = models.IntegerField('mục', choices=ITEM_CHOICES)
    title = models.TextField('tiêu đề')
    legal_basis = RichTextField('căn cứ, đề xuất, ý nghĩa', blank=True, null=True)
    note = RichTextField('ghi chú', blank=True, null=True)
    files = models.ManyToManyField('File',verbose_name='file căn cứ', blank=True)

    class Meta:
        verbose_name  = 'tiêu chí'
        verbose_name_plural  = 'tiêu chí'    
    
    def __str__(self):
        return f'{self.section_chapter}.{self.evaluation_criteria}'

# Mức chất lượng
class Level(models.Model):
    LEVEL_CHOICES = (
        (1, 'Mức 1'),
        (2, 'Mức 2'),
        (3, 'Mức 3'),
        (4, 'Mức 4'),
        (5, 'Mức 5'),
    )
    evaluation_criteria = models.ForeignKey(EvaluationCriteria, verbose_name='tiêu chí', on_delete=models.CASCADE)
    level = models.IntegerField(choices = LEVEL_CHOICES, verbose_name='mức độ đánh giá')

    class Meta:
        verbose_name  = 'mức chất lượng'
        verbose_name_plural  = 'mức chất lượng'
    
    def __str__(self):
        return f'{self.evaluation_criteria}. {self.get_level_display()}'
    
# Tiểu mục trong từng tiêu chí
class Condition(models.Model):

    evaluation_criteria_level = models.ForeignKey(Level, verbose_name='mức chất lượng', on_delete=models.CASCADE)
    index = models.IntegerField()
    title = models.TextField()

    class Meta:
        verbose_name  = 'tiểu mục trong tiêu chí'
        verbose_name_plural  = 'tiểu mục trong tiêu chí'

    def assessment_condition_name(self):
        return f'{self.assessmentcondition.is_pass}'




    def __str__(self):
        return f'{self.evaluation_criteria_level.evaluation_criteria} - Tiểu mục {self.index}({self.evaluation_criteria_level.get_level_display()})'

# Upload file
class File(models.Model):
    description = models.CharField(max_length=200)
    file = models.FileField(upload_to='doccuments/')
    class Meta:
        verbose_name  = 'file đính kèm'
        verbose_name_plural  = 'file đính kèm'  

    def __str__(self):
        return f'{self.description}'
    
# Upload Image
class Image(models.Model):
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')  
    

    def __str__(self):
        return f'{self.description}'
    
    class Meta:
        verbose_name  = 'ảnh đính kèm'
        verbose_name_plural  = 'ảnh đính kèm' 
    


# Người chịu trách nhiệm quản lý tiêu chí
class Responser(models.Model):
    time_created = models.DateField(auto_now=True, blank=True, null=True)
    user = models.ForeignKey('HQMMember', verbose_name='thành viên' , on_delete=models.CASCADE)
    evalution_criteria = models.ForeignKey(EvaluationCriteria, verbose_name='tiêu chí', on_delete=models.CASCADE)
    ROLE_CHOICES = (
        (1, 'Phụ trách chính'),
        (2, 'Phụ tránh chung'),
    )
    role = models.IntegerField(choices=ROLE_CHOICES, verbose_name="vai trò")
    notes = models.CharField(max_length=200 ,blank=True, null=True, verbose_name='ghi chú')
    class Meta:
        verbose_name  = 'người phụ trách tiêu chí'
        verbose_name_plural  = 'người phụ trách tiêu chí'    


# Người chịu trách nhiệm tiểu mục trong tiêu chí
class ResponserCondition(models.Model):
    time_created = models.DateField(auto_now=True, blank=True, null=True)
    member = models.ForeignKey('HQMMember', verbose_name='người phụ trách' , on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, verbose_name='tiểu mục', on_delete=models.CASCADE)
    ROLE_CHOICES = (
        (1, 'Phụ trách chính'),
        (2, 'Phụ tránh chung'),
    )
    role = models.IntegerField(choices=ROLE_CHOICES, verbose_name='vai trò')
    notes = models.CharField(blank=True, null=True, verbose_name='ghi chú', max_length=1000)
    class Meta:
        verbose_name  = 'người phụ trách tiểu mục'
        verbose_name_plural  = 'người phụ trách tiểu mục'    


# Tự đánh giá các tiêu chí
class Assessment(models.Model):
    LEVEL_CHOICES = (
        (1, 'Mức 1'),
        (2, 'Mức 2'),
        (3, 'Mức 3'),
        (4, 'Mức 4'),
        (5, 'Mức 5'),
    )
    date_created = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name='thời gian tạo')
    date_updated = models.DateField(auto_now=True, blank=True, null=True, verbose_name='thòi gian cập nhật')
    responser = models.ForeignKey('HQMMember', verbose_name="người đánh giá", on_delete=models.CASCADE)
    evaluation_criteria = models.OneToOneField(EvaluationCriteria, verbose_name='tiêu chí', on_delete=models.CASCADE)
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name="mức đánh giá")

    note = models.CharField(blank=True, null=True, verbose_name='Ghi chú', max_length=1000)
    class Meta:
        verbose_name  = 'đánh giá tiêu chí'
        verbose_name_plural  = 'đánh giá tiêu chí'
    
    def color_level(self):
        if self.level < 3: return 'text-danger'
        if self.level > 2 and self.level < 5: return 'text-warning'
        if self.level > 4: return 'text-success'

    def remain(self):
        return 5 - self.level
    def __str__(self):
        return f'{self.get_level_display()}'

# Tự đánh giá tiểu mục
class AssessmentCondition(models.Model):
    time_created = models.DateTimeField(auto_now=True)
    time_updated = models.DateTimeField(auto_now_add=True)
    responser = models.ForeignKey('HQMMember', verbose_name="người đánh giá", on_delete=models.CASCADE)
    is_pass = models.BooleanField(default=False, verbose_name='đạt hay chưa?')
    condition = models.OneToOneField(Condition, verbose_name='tiểu mục', on_delete=models.CASCADE)
    notes = models.CharField(max_length=1000, verbose_name='ghi chú', blank=True, null=True)
    files = models.ManyToManyField(File, verbose_name='file đính kèm', blank=True)
    images = models.ManyToManyField(Image, verbose_name='ảnh đính kèm', blank=True)



    class Meta:
        verbose_name  = 'đánh giá tiểu mục'
        verbose_name_plural  = 'đánh giá tiểu mục'

# Thành viên nhóm quản lý chất lượng bệnh viện
class HQMMember(models.Model):
    member = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='nhân viên')
    date_joined = models.DateField(auto_now=True)
    ROLE_CHOICES = (
        (1, 'Quản lý'),
        (2, 'Thành viên'),
    )

    role = models.IntegerField(choices=ROLE_CHOICES, verbose_name='Vai trò')
    note = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ghi chú')

    class Meta:
        verbose_name  = 'thành viên nhóm QLCLBV'
        verbose_name_plural  = 'thành viên nhóm QLCLBV'
    
    def __str__(self):
        return f'{self.member} - {self.get_role_display()}'