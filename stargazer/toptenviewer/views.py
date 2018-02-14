from django.http import HttpResponse

from toptenfetcher.models import GitHubLanguage, GitHubRankedRepo


def index(request):
    languages = GitHubLanguage.objects.all()
    languages_str = "<br/>".join([
        language.name
        for language in languages
    ])

    repos = GitHubRankedRepo.objects.all()
    repos_str = "<br/>".join([
        str(repo)
        for repo in repos
    ])

    return HttpResponse(
        "<h1>Languages</h1>{}<h1>Repos</h1>{}".format(
            languages_str, repos_str))
