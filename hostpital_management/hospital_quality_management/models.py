from django.db import models


# Models for Hospital Quality Management - HRM

# Tiêu chí đánh giá
class EvaluationCriteria(models.Model):
    index = models.CharField(max_length=4)
    title = models.CharField(max_length=1000)
    legal_basis = models.TextField()