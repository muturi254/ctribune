from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    class Meta:
        ordering = ['first_name']
    # cange representation of data to string readable
    def __str__(self):
        return self.first_name