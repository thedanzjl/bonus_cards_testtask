from django.db import models


class Cards(models.Model):
    STATUS_CHOICES = (
        ('not activated', 'not activated'),
        ('activated', 'activated'),
        ('overdue', 'overdue')
    )
    series = models.IntegerField()
    number = models.IntegerField()
    release_date = models.DateField()
    activity_end_date = models.DateField()
    usage_date = models.DateField()
    status = models.CharField(max_length=13, choices=STATUS_CHOICES)

