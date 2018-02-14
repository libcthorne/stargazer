import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from toptenfetcher.models import GitHubLanguage


SEARCH_PAGE_URL = "https://github.com/search/advanced"


class Command(BaseCommand):
    help = "Fetches all known programming languages on GitHub"

    def handle(self, *args, **options):
        self.stdout.write("Fetching GitHub programming languages")
        clear_github_languages()
        save_github_languages()


def clear_github_languages():
    GitHubLanguage.objects.all().delete()

def save_github_languages():
    search_page = requests.get(SEARCH_PAGE_URL)
    soup = BeautifulSoup(search_page.text, "html.parser")
    language_names = sorted([
        o["value"]
        for o in soup.find(id="search_language").find_all("option")
        if o["value"] != ""
    ], key=str.lower)

    for language_name in language_names:
        print("Found {}".format(language_name))
        language = GitHubLanguage(name=language_name)
        language.save()
