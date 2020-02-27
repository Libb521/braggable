from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=60)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.TextField(max_length=510)
    tags = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=60, unique=True)

    class tags(models.Model):
        name = models.CharField(max_length =30)

    def __unicode__(self):
        return self.title

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='albums', null=True)
    # album = models.ForeignKey('album', on_delete=models.PROTECT)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    