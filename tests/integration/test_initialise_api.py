import os
import pytest
from modules.apiHandler import initialise_api, get_github_instance, get_organisation, get_repo

# --- Valid Variables ---
valid_token = str(os.getenv('GH_API_TOKEN'))
valid_org_username = 'codeowners-rfc-test'
valid_repo_name = 'testing-repo'

# --- Valid Returns ---
gh_instance = get_github_instance(valid_token)
org = get_organisation(gh_instance, valid_org_username)
repo = get_repo(org, valid_repo_name)

# --- Invalid Variables ---
invalid_token = 'invalid_token'
invalid_org_username = 'invalid_org_username'
invalid_repo_name = 'invalid_repo_name'

def test_initialise_api_with_all_valid_variables() -> None:
  # Given valid variables
  g, o, r = initialise_api(valid_token, valid_org_username, valid_repo_name)
  assert g.get_user().login == gh_instance.get_user().login
  assert o == org
  assert r == repo

def test_initialise_api_with_all_invalid_variables() -> None:
  # Given all invalid variables
  assert initialise_api(invalid_token, invalid_org_username, invalid_repo_name) == None

def test_initialise_api_with_invalid_token() -> None:
  # Given all invalid token
  assert initialise_api(invalid_token, valid_org_username, valid_repo_name) == None

def test_initialise_api_with_invalid_org_username() -> None:
  # Given all invalid org_username
  assert initialise_api(valid_token, invalid_org_username, valid_repo_name) == None

def test_initialise_api_with_invalid_repo_name() -> None:
  # Given all invalid repo_name
  assert initialise_api(valid_token, valid_org_username, invalid_repo_name) == None