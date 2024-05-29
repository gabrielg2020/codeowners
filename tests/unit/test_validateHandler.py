import os
import pytest
from github import Github, Auth
from modules import validate_api_token, validate_org_name

token = str(os.getenv("GH_API_TOKEN"))
org_name = str(os.getenv("ORG_NAME"))

auth = Auth.Token(token)
github_instance = Github(auth=auth)
github_login_name = github_instance.get_user().login

org = github_instance.get_organization(org_name)

def test_validate_api_token() -> None:
  # Given a valid API token
  assert validate_api_token(token).get_user().login == github_login_name # type: ignore
  # Given an invalid API token
  assert validate_api_token('Non_Valid_API_Token') == None

def test_validate_org_name() -> None:
  # Given a valid organisation name
  assert validate_org_name(github_instance, org_name).name == org.name # type: ignore
  # Given an invalid organisation name
  assert validate_org_name(github_instance, "Non_Valid_Org_Name") == None