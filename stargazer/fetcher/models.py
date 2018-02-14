from django.db import models


class GitHubLanguage(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class GitHubRankedRepo(models.Model):
    name = models.CharField(max_length=200)
    stargazers = models.PositiveIntegerField()
    language = models.ForeignKey(GitHubLanguage,
        on_delete=models.CASCADE)

    def __str__(self):
        return "[{}] {}: {} stars".format(
            self.language, self.name, self.stargazers)
