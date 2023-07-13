from django.db import models

from CMS_project import settings


class BlogModel(models.Model):
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    content=models.CharField(max_length=500)
    created_date=models.DateField(auto_now=True)

    class Meta:
        db_table="blog_table"

class LikeModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)

    class Meta:
        db_table="like_table"

