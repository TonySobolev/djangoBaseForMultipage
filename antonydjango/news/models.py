from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Article_Name')
    date = models.DateTimeField('Date_Public')

    def __str__(self):
        return f'News for today : {self.title}'

    class Meta:
        verbose_name ='Article'
        verbose_name_plural = 'All Articles'
