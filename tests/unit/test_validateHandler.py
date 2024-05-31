import os
import pytest
from github import Github, Auth
from modules import validate_api_token, validate_org_username, validate_github_repo, validate_file

# --- Auth Variables ---
token = str(os.getenv("GH_API_TOKEN"))
auth = Auth.Token(token)

# --- Variables Used To Test ---
org_name = "codeowners-rfc-test"
repo_name = "testing-repo"
file_name = "test-file"

gh_instance = Github(auth=auth)
org = gh_instance.get_organization(org_name)
repo = org.get_repo(repo_name)
file = repo.get_contents(file_name)

def test_validate_api_token() -> None:
  # Given a valid API token
  assert validate_api_token(token).get_user() == gh_instance.get_user() # type: ignore
  # Given an invalid API token
  assert validate_api_token('non_valid_api_token') == None

def test_validate_org_username() -> None:
  # Given a valid organisation name
  assert validate_org_username(gh_instance, org_name) == org
  # Given an invalid organisation name
  assert validate_org_username(gh_instance, "non_valid_org_username") == None

def test_validate_github_repo() -> None:
  # Given a valid repo within an organisation
  assert validate_github_repo(org, repo_name) == repo
  # Given an invalid repo within an organisation
  assert validate_github_repo(org, "non_valid_repo_name") == None

def test_validate_file() -> None:
  # Given a valid file within repo
  assert validate_file(repo, file_name) == file
  # Given an invalid file within repo
  assert validate_file(repo, "non_valid_file_name") == None