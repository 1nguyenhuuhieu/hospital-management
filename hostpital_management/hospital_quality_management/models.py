from django.db import models


# Models for Hospital Quality Management - HRM

# Phần tiêu chí đánh giá
class Section(models.Model):
    index = models.CharField(max_length=1)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.index

# Chương tiêu chí đánh giá
class Chapter(models.Model):
    index = models.IntegerField()
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.index

# Tiêu chuẩn đánh giá
class EvaluationCriteria(models.Model):
    index = models.IntegerField()
    title = models.TextField()
    legal_basis = models.TextField()
    def __str__(self):
        return self.index

# Mức đánh giá
class Level(models.Model):
    LEVEL_CHOICES = (
        (1, 'Mức 1'),
        (2, 'Mức 2'),
        (3, 'Mức 3'),
        (4, 'Mức 4'),
        (5, 'Mức 5'),
        (6, 'Mức 6'),
        (7, 'Mức 7'),
        (8, 'Mức 8'),
        (9, 'Mức 9'),
        (10, 'Mức 10'),
    )
    index = models.IntegerField(choices = LEVEL_CHOICES)
    title = models.CharField(max_length=1000)
    def __str__(self):
        return self.index

    