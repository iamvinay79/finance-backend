from django.db import models

class Record(models.Model):
    TYPE_CHOICES = [
        ("income", "Income"),
        ("expense", "Expense"),
    ]

    amount = models.FloatField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=100)
    date = models.DateField()
    notes = models.TextField(blank=True)