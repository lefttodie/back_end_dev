import requests
from app.core.config import GITHUB_TOKEN
from fastapi import HTTPException

BASE_URL = "https://api.github.com"

def get_headers():
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

# 🔹 Fetch Repositories
def fetch_repos(username: str):
    url = f"{BASE_URL}/users/{username}/repos"

    response = requests.get(url, headers=get_headers())

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.json()
        )

    return response.json()


# 🔹 Create Issue
def create_issue(owner: str, repo: str, title: str, body: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"

    payload = {
        "title": title,
        "body": body
    }

    response = requests.post(url, json=payload, headers=get_headers())

    if response.status_code != 201:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.json()
        )

    return response.json()


# 🔹 List Issues
def list_issues(owner: str, repo: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"

    response = requests.get(url, headers=get_headers())

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.json()
        )

    return response.json()