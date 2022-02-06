from django.db import models

class Book(models.Model):
    GENRE = [
        ('ROMANCE','ROMANCE'),
        ('FICTION','FICTION'),
        ('ACTION','ACTION'),
        ('ADVENTURE','ADVENTURE'),
        ('COMEDY','COMEDY')
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    genre = models.CharField(choices=GENRE, max_length=10)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    count = models.IntegerField()

    def __str__(self):
        return self.title