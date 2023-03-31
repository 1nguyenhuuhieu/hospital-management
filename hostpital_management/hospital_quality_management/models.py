from django.db import models
from ckeditor.fields import RichTextField


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
    legal_basis = RichTextField('Căn cứ, đề xuất, ý nghĩa',)
    files = models.ManyToManyField('File', blank=True)

    class Meta:
        verbose_name  = 'Tiêu chí'
        verbose_name_plural  = 'Tiêu chí'    

    def __str__(self):
        return f'{self.pre_index.pre_index.index}{self.pre_index.index}{self.index}: {self.title}'
    

class RequestLevel(models.Model):
    LEVEL_CHOICES = (
        (1, 'Mức 1'),
        (2, 'Mức 2'),
        (3, 'Mức 3'),
        (4, 'Mức 4'),
        (5, 'Mức 5'),
    )
    pre_index = models.ForeignKey(EvaluationCriteria, verbose_name='Tiêu chí', on_delete=models.CASCADE)
    level = models.IntegerField(choices = LEVEL_CHOICES, verbose_name='Mức độ đánh giá')
    index = models.IntegerField(verbose_name='Bậc')
    title = models.TextField(verbose_name='Nội dung')

    class Meta:
        verbose_name  = 'Bậc thang chất lượng'
        verbose_name_plural  = 'Bậc thang chất lượng'
    def __str__(self):
        return f'{self.index}. {self.title}'

# Upload file
class File(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='doccument/')
    class Meta:
        verbose_name  = 'File đính kèm'
        verbose_name_plural  = 'File đính kèm'    
