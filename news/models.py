from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datearchived = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='news/images/')
    url = models.URLField(blank=True)
    newscreator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        ordering = ['-created']


    def __str__(self):
        return self.title


class Comments(models.Model):
    commentlocation = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE, db_constraint=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    info = models.TextField(verbose_name='текст комментария')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['-created']

    #def __str__(self):
        #return "%s (%s) - %s" % (self.info, self.commentlocation.newscreator, self.commentlocation.title)
