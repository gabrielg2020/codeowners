import os
import pytest
from github import Github, Auth
from modules import get_github_instance, get_organisation, get_repo, get_file

# --- Auth Variables ---
token = str(os.getenv("GH_API_TOKEN"))
auth = Auth.Token(token)
gh_instance = Github(auth=auth)

# --- Variables Used To Test ---
login_name = "gabrielg2020"
org_name = "codeowners-rfc-test"
repo_name = "testing-repo"
file_name = "test-file"

login = gh_instance.get_user().login
org = gh_instance.get_organization(org_name)
repo = org.get_repo(repo_name)
file = repo.get_contents(file_name)

def test_get_github_instance() -> None: # This makes API calls to test if token is valid
  # Given a valid API token
  assert get_github_instance(token).get_user().login == login_name # type: ignore
  # Given an invalid API token
  assert get_github_instance('non_valid_api_token') is None

def test_get_organisation() -> None:
  # Given a valid organisation name
  assert get_organisation(gh_instance, org_name) == org
  # Given an invalid organisation name
  assert get_organisation(gh_instance, "non_valid_org_username") is None

def test_get_repo() -> None:
  # Given a valid repo within an organisation
  assert get_repo(org, repo_name) == repo
  # Given an invalid repo within an organisation
  assert get_repo(org, "non_valid_repo_name") is None

def test_get_file() -> None:
  # Given a valid file within repo
  assert get_file(repo, file_name) == file
  # Given an invalid file within repo
  assert get_file(repo, "non_valid_file_name") is None