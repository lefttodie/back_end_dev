from fastapi import APIRouter
from app.services.github_service import fetch_repos, create_issue, list_issues
from app.models.schemas import IssueCreate

router = APIRouter(prefix="/github", tags=["GitHub"])

#  Get repos
@router.get("/repos/{username}")
def get_repositories(username: str):
    return fetch_repos(username)

#  Create issue
@router.post("/create-issue")
def create_issue_api(issue: IssueCreate):
    return create_issue(
        issue.owner,
        issue.repo,
        issue.title,
        issue.body
    )

#  List issues
@router.get("/issues/{owner}/{repo}")
def get_issues(owner: str, repo: str):
    return list_issues(owner, repo)