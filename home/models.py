from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    release_date = models.DateField()
    # aur jo bhi fields tum chaho

    def __str__(self):
        return self.title
