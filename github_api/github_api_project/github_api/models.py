from django.db import models

# Create your models here.


class GitHubRepository(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    stars = models.IntegerField()

    def __str__(self):
        return self.name
