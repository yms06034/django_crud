from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=50)
    published_date = models.DateField()

    def __str__(self):
        return self.name