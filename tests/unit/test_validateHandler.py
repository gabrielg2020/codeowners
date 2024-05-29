import os
import pytest
from github import Github, Auth
from modules import validate_api_key

key = str(os.getenv("GH_API_KEY"))

def test_validate_api_key() -> None:
  # Given a valid API key
  auth = Auth.Token(key)
  github_instance = Github(auth=auth)
  github_login_name = github_instance.get_user().login
  assert validate_api_key(key).get_user().login == github_login_name # type: ignore
  # Given an invalid API key
  assert validate_api_key('None_Valid_API_Key') == None

