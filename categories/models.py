from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)

    # to capitalize the first latter
    def clean(self):
        self.category = self.category.capitalize()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category
