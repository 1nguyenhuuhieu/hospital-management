from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Models for Hospital Quality Management - HRM

# Phần tiêu chí đánh giá
class Section(models.Model):
    SECTION_CHOICES = (
        ('A', 'Phần A'),
        ('B', 'Phần B'),
        ('C', 'Phần C'),
        ('D', 'Phần D'),
        ('E', 'Phần E'),
        ('F', 'Phần F'),
        ('G', 'Phần G')
    )
    index = models.CharField('Phần', max_length=1, choices=SECTION_CHOICES)
    title = models.TextField('Tiêu đề')

    class Meta:
        verbose_name  = 'Phần'
        verbose_name_plural  = 'Phần'


    def __str__(self):
        return f'{self.index}: {self.title}'

# Chương tiêu chí đánh giá
class Chapter(models.Model):
    pre_index = models.ForeignKey(Section,verbose_name='Phần', on_delete=models.CASCADE)
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
    index = models.IntegerField('Chương', choices=CHAPTER_CHOICES)
    title = models.TextField('Tiêu đề')
    
    class Meta:
        verbose_name  = 'Chương'
        verbose_name_plural  = 'Chương'

    def __str__(self):
        return f'{self.pre_index.index}{self.index}: {self.title}'

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
    pre_index = models.ForeignKey(Chapter, verbose_name='Phần, Chương', on_delete=models.CASCADE)
    index = models.IntegerField('Mục', choices=ITEM_CHOICES)
    title = models.TextField('Tiêu đề')
    legal_basis = RichTextField('Căn cứ, đề xuất, ý nghĩa', blank=True, null=True)
    note = RichTextField('Ghi chú', blank=True, null=True)
    files = models.ManyToManyField('File', blank=True)

    def index_name(self):
        return f'{self.pre_index.pre_index.index}{self.pre_index.index}{self.index}'

    class Meta:
        verbose_name  = 'Tiêu chí'
        verbose_name_plural  = 'Tiêu chí'    

    def __str__(self):
        return f'{self.pre_index.pre_index.index}{self.pre_index.index}{self.index}: {self.title}'

# Mức chất lượng
class Level(models.Model):
    LEVEL_CHOICES = (
        (1, 'Mức 1'),
        (2, 'Mức 2'),
        (3, 'Mức 3'),
        (4, 'Mức 4'),
        (5, 'Mức 5'),
    )
    pre_index = models.ForeignKey(EvaluationCriteria, verbose_name='Tiêu chí', on_delete=models.CASCADE)
    level = models.IntegerField(choices = LEVEL_CHOICES, verbose_name='Mức độ đánh giá')

    class Meta:
        verbose_name  = 'Mức chất lượng'
        verbose_name_plural  = 'Mức chất lượng'

    
# Điều kiện của từng mức chất lượng
class Condition(models.Model):

    pre_index = models.ForeignKey(Level, verbose_name='Mức chất lượng', on_delete=models.CASCADE)
    index = models.IntegerField()
    title = models.TextField()

    class Meta:
        verbose_name  = 'Bậc thang từng mức chất lượng'
        verbose_name_plural  = 'Bậc thang từng mức chất lượng'
    def __str__(self):
        return f'{self.index}'

# Upload file
class File(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='doccument/')
    class Meta:
        verbose_name  = 'File đính kèm'
        verbose_name_plural  = 'File đính kèm'    

# Người chịu trách nhiệm quản lý
class Responser(models.Model):
    time_created = models.DateField(auto_now=True, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='Nhân viên' , on_delete=models.CASCADE)
    evalution_criteria = models.ForeignKey(EvaluationCriteria, verbose_name='Tiêu chí', on_delete=models.CASCADE)
    ROLE_CHOICES = (
        (1, 'Phụ trách chính'),
        (2, 'Phụ tránh chung'),
    )
    role = models.IntegerField(choices=ROLE_CHOICES)
    notes = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name  = 'Người phụ trách'
        verbose_name_plural  = 'Người phụ trách'    
    def __str__(self):
        return f'{self.evalution_criteria.index_name()}. {self.user}'

# Bằng chứng tiêu chí
class Proof(models.Model):
    time_created = models.DateTimeField(auto_now=True)
    time_updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='Người tải lên', on_delete=models.CASCADE)
    evalution_criteria = models.ForeignKey(EvaluationCriteria, verbose_name='Tiêu chí', on_delete=models.CASCADE)
    files = models.ManyToManyField('File', blank=True)
    notes = RichTextField()