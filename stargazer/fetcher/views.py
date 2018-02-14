from django.http import HttpResponse

from .models import GitHubLanguage


def index(request):
    languages = GitHubLanguage.objects.all()
    languages_str = "<br/>".join([
        language.language
        for language in languages
    ])
    return HttpResponse(languages_str)
