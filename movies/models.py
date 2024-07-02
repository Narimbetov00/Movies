from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100,unique=True)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse('movies:cotegory',args=[self.slug])
 
class Movies(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    realised_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    trailer = models.URLField(verbose_name='link',blank=True)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('movies:movie',args=[self.id,self.slug])