import os
import sys

import requests
from django.core.management.base import BaseCommand
from django.db import transaction

from toptenfetcher.models import (
    GitHubLanguage,
    GitHubRankedRepo,
)


API_URL = "https://api.github.com/graphql"

try:
    OAUTH_TOKEN = os.environ["OAUTH_TOKEN"]
except KeyError:
    sys.stderr.write("OAUTH_TOKEN not specified\n")
    sys.exit(1)


class Command(BaseCommand):
    help = "Fetches top ten GitHub repos for all registered languages"

    def handle(self, *args, **options):
        for language in GitHubLanguage.objects.all():
            self.stdout.write("Fetching top ten repos for {}".format(language.name))

            with transaction.atomic():
                clear_top_ten_repos_for_language(language)
                save_top_ten_repos_for_language(language)


def clear_top_ten_repos_for_language(language):
    GitHubRankedRepo.objects.filter(language=language).delete()

def save_top_ten_repos_for_language(language):
    r = requests.post(API_URL, json={
        "query": """
          query($query:String!) {
            search(query: $query, type: REPOSITORY, first: 10) {
              edges {
                node {
                  ... on Repository {
                    description
                    nameWithOwner
                    url
                    stargazers {
                      totalCount
                    }
                  }
                }
              }
            }
          }
        """,
        "variables": {
            "query": f"language:{language.name} sort:stars-desc"
        }
    }, headers={"Authorization": f"token {OAUTH_TOKEN}"})

    search_results = r.json()["data"]["search"]["edges"]

    for search_result in search_results:
        repo_data = search_result["node"]
        repo = GitHubRankedRepo(
            name=repo_data["nameWithOwner"],
            stargazers=repo_data["stargazers"]["totalCount"],
            language=language,
        )
        repo.save()
