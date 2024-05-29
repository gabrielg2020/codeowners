import os
import pytest
from github import Github, Auth
from modules import validate_api_token

token = str(os.getenv("GH_API_TOKEN"))

def test_validate_api_token() -> None:
  # Given a valid API token
  auth = Auth.Token(token)
  github_instance = Github(auth=auth)
  github_login_name = github_instance.get_user().login
  assert validate_api_token(token).get_user().login == github_login_name # type: ignore
  # Given an invalid API token
  assert validate_api_token('None_Valid_API_token') == None

