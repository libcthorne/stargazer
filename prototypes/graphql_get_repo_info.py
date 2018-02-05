import os
import sys

import requests

API_URL = "https://api.github.com/graphql"

try:
    OAUTH_TOKEN = os.environ["OAUTH_TOKEN"]
except KeyError:
    print("OAUTH_TOKEN not specified")
    sys.exit(1)

r = requests.post(API_URL, json={
    "query": """
      query($pinned_repos_count:Int!) {
        repository(owner: "libcthorne", name: "stargazer") {
          createdAt
          description
          url
          owner {
            login
            pinnedRepositories(first:$pinned_repos_count) {
              edges {
                node {
                  url
                }
              }
            }
            url
          }
        }
      }
    """,
    "variables": {
        "pinned_repos_count": 4
    }
}, headers={"Authorization": "token {}".format(OAUTH_TOKEN)})

print(r.text)
