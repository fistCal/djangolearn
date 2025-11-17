from django.db import models
from django.utils import timezone

# Create your models here.
class testappVariety(models.Model):
    TEST_TYPE_CHOICE = [
        ('MD', 'Middle'),
        ('WD', 'Window'),
        ('AL', 'Aile'),
    ]
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='testapps/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=TEST_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name 