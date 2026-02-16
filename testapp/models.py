from django.db import models

from django.utils import timezone



class Post(models.Model):

    title = models.CharField('Title', max_length=200)

    text = models.TextField('Text')

    created_date = models.DateTimeField('Created date', default=timezone.now)

    

    def __str__(self):

        return self.title

    

    class Meta:

        verbose_name = 'Post'

        verbose_name_plural = 'Posts'
