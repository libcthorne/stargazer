from django.shortcuts import render

from fetcher.models import GitHubLanguage, GitHubRankedRepo


def index(request):
    return render(request, "viewer/index.html", {
        "languages": GitHubLanguage.objects.all(),
        "repos": GitHubRankedRepo.objects.all(),
    })