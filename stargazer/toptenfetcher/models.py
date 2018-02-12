from django.db import models


class GitHubLanguage(models.Model):
    language = models.CharField(max_length=200)

    def __str__(self):
        return self.language
