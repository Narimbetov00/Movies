from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your models here.


# Filmlerdi Kategoriyaga boliw ushin Birinshi nawbette Kategoriya Modeli jaratip alindi
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100,unique=True)

    #Bul jerde Meta Classdin waziypasi admin Bolimindegi korinisi ushin verbose_name  berilgen
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    # funksiya str bul har bir qosilgan kategoryalar ati menen koriniwi ushin jazilgan
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse('movies:cotegory',args=[self.slug])
 

# class Movies bul class Category menen jalganip Filimlerdi Saqlaw ushin Model jaratilgan
class Movies(models.Model):
    name = models.CharField(max_length=255) #max_length bul kiritiliwi kerek bolgan maksimal belgiler sanin belgileydi
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #ForeignKey arqali Category clasina jalgandi
    realised_date = models.DateField() # Base ge magliwmat tusken waqit
    description = models.TextField()  #Bizdin filmge bergen magliwmatimiz
    image = models.ImageField(upload_to='images/') # film suwretleri. upload_to='images/' Bul bolsa media file ishinde avto jaratilatigin file birinshi nawbette sizde media file boliwi kerek
    trailer = models.URLField(verbose_name='link',blank=True)   # Bul Filmden qisqa metraj.blank=True din waziypasi Kiritbew imkaniyatina iye boliw

    #Bul jerde Meta Classdin waziypasi admin Bolimindegi korinisi ushin verbose_name  berilgen
    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    # funksiya str bul har bir qosilgan Movies ati menen koriniwi ushin jazilgan
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('movies:movie',args=[self.id,self.slug])
    
# class Comments bul Movies penen birgelikte jalgangan 
class Comments(models.Model):
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE,related_name='comments',blank=True,null=True) #related_name='comments' bul comentsti basqa filelarda shaqiriw imkanin beredi
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True) #auto_now_add=True Bizden waqitti soramastan avto sol waqitti kiritedi
    author = models.CharField(max_length=150)