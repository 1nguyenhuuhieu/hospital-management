from django.db import models


# Models for Hospital Quality Management - HRM

# Phần tiêu chí đánh giá
class SectionCriteria(models.Model):
    index = models.CharField(max_length=1)
    title = models.CharField(max_length=200)

class EvaluationCriteria(models.Model):
    index_letter = models.CharField(max_length=4)
    index_number1= models.CharField(max_length=4)
    index_number2 = models.CharField(max_length=4)
    title = models.CharField(max_length=1000)
    legal_basis = models.TextField()