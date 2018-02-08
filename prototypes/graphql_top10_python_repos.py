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
        "query": "language:python sort:stars-desc"
    }
}, headers={"Authorization": "token {}".format(OAUTH_TOKEN)})

print(r.text)
