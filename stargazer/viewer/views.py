from django.shortcuts import get_object_or_404, render

from fetcher.models import GitHubLanguage, GitHubRankedRepo


def index(request):
    return render(request, "viewer/index.html")

def repos_show(request):
    language_name = request.GET.get("language")
    language = get_object_or_404(
        GitHubLanguage,
        name__iexact=language_name,
    )
    repos = GitHubRankedRepo.objects.filter(
        language=language,
    )

    return render(request, "viewer/repos_show.html", {
        "language": language,
        "repos": repos,
    })
