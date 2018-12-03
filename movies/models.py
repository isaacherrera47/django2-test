from django.conf import settings
from django.db import models


# Create your models here.
class Review(models.Model):
    """
    Model Review to add reviews which could be commented by registered users
    """
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=500)
    poster = models.ImageField(upload_to='%Y/%m/%d/')
    review = models.CharField(max_length=500)
    release_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-release_date',)


class Comment(models.Model):
    """
    Model Comment to add comments about a review.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=255)

    def __str__(self):
        return self.comment
