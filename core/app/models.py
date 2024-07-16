from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Music(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    file = models.FileField(upload_to='media/musics')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    music_text = models.TextField()

    def __str__(self):
        return self.title

