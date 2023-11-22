from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    amount = models.IntegerField(default=1000)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "post"