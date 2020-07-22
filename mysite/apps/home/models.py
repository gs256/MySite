from django.db import models


class Article(models.Model):
    image = models.ImageField('Article preview', upload_to='article_images/', default='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Roundel_of_None.svg/600px-Roundel_of_None.svg.png')
    title = models.CharField('Article title', max_length=255)
    text = models.TextField('Article text')
    date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comment(models.Model):
    parent_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField("Author's name", max_length=50)
    user_icon = models.ImageField('User icon', upload_to='user_icons/', default='defaults/unknown.png')
    text = models.CharField('Comment text', max_length=255)
    parent_comment = models.ForeignKey('self', verbose_name='Parent comment', on_delete=models.SET_NULL, blank=True, null=True)
    number_of_likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'