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
    "query": """{
      repository(owner: \"libcthorne\", name: "stargazer") {
        createdAt
        description
        url
        owner {
          login
          pinnedRepositories(first:4) {
            edges {
              node {
                url
              }
            }
          }
          url
        }
      }
    }"""}, headers={"Authorization": "token {}".format(OAUTH_TOKEN)})

print(r.text)
