import os
import pytest
from github import Github, Auth
from modules import validate_api_token, validate_org_username

token = str(os.getenv("GH_API_TOKEN"))
org_username = str(os.getenv("org_username"))

auth = Auth.Token(token)
gh_instance = Github(auth=auth)
gh_login_name = gh_instance.get_user().login

org = gh_instance.get_organization(org_username)

def test_validate_api_token() -> None:
  # Given a valid API token
  assert validate_api_token(token).get_user().login == gh_login_name # type: ignore
  # Given an invalid API token
  assert validate_api_token('Non_Valid_API_Token') == None

def test_validate_org_username() -> None:
  # Given a valid organisation name
  assert validate_org_username(gh_instance, org_username).name == org.name # type: ignore
  # Given an invalid organisation name
  assert validate_org_username(gh_instance, "Non_Valid_org_username") == None