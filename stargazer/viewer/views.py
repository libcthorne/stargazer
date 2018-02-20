from django.shortcuts import get_object_or_404, render
from django.utils.safestring import mark_safe

from fetcher.models import GitHubLanguage, GitHubRankedRepo


def index(request):
    language_names = [
        language.name
        for language in GitHubLanguage.objects.all()
    ]

    return render(request, "viewer/index.html", {
        "language_names": language_names,
    })

def repos_show(request):
    language_name = request.GET.get("language")

    try:
        language = GitHubLanguage.objects.get(name__iexact=language_name)
    except GitHubLanguage.DoesNotExist:
        language = None
        repos = None
    else:
        repos = GitHubRankedRepo.objects.filter(
            language=language,
        )

    return render(request, "viewer/repos_show.html", {
        "language": language,
        "repos": repos,
    })
