from django.db import models

# Create your models here.
class Category(models.Model):
    catogary_name=models.CharField(unique=True, max_length=50)
    slug=models.CharField(unique=True,max_length=100)
    description=models.TextField(blank=True,max_length=255)
    cat_image=models.ImageField(upload_to="photos/categories",blank=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
        return self.catogary_name
    

