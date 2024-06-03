import os
import pytest
from github import Github, Auth
from modules.apiHandler import get_github_instance, get_organisation, get_repo, get_file, get_members, get_repos, validate_co_history_file

# --- Auth Variables ---
token = str(os.getenv('GH_API_TOKEN'))
auth = Auth.Token(token)
gh_instance = Github(auth=auth)

# --- Variables Used To Test ---
login_name = 'gabrielg2020'
org_name = 'codeowners-rfc-test'
repo_name = 'testing-repo'
file_name = 'test_file'
members = ['gabrielg2020', 'testacc03']
repos = ['cool-project', 'facebook2', 'testing-repo']
valid_json_file_name = 'valid.json'
invalid_json_file_name = 'invalid.json'
co_history_file_name = 'valid_co_history.json'

login = gh_instance.get_user().login
org = gh_instance.get_organization(org_name)
repo = org.get_repo(repo_name)
file = repo.get_contents(file_name)
valid_json_file = repo.get_contents(valid_json_file_name)
invalid_json_file = repo.get_contents(invalid_json_file_name)
co_history_file = repo.get_contents(co_history_file_name)
co_history_file_contents = {
  "developers": [
    {"acc_name":"gabrielg2020",
      "number_of_times_co": 2,
      "current_repo": "facebook2",
      "repos": [
        "testing-repo",
        "facebook2"
      ]
    }
  ]
}

def test_get_github_instance() -> None: # This makes API calls to test if token is valid
  # Given a valid API token
  assert get_github_instance(token).get_user().login == login_name
  # Given an invalid API token
  assert get_github_instance('non_valid_api_token') is None

def test_get_organisation() -> None:
  # Given a valid organisation name
  assert get_organisation(gh_instance, org_name) == org
  # Given an invalid organisation name
  assert get_organisation(gh_instance, 'non_valid_org_username') is None

def test_get_repo() -> None:
  # Given a valid repo within an organisation
  assert get_repo(org, repo_name) == repo
  # Given an invalid repo within an organisation
  assert get_repo(org, 'non_valid_repo_name') is None

def test_get_file() -> None:
  # Given a valid file within repo
  assert get_file(repo, file_name) == file
  # Given an invalid file within repo
  assert get_file(repo, 'non_valid_file_name') is None
  # Given a directory name within repo
  assert get_file(repo, 'test-dir') is None

def test_get_members() -> None:
  # Given a valid organisation
  assert get_members(org) == members
  # Given an invalid organisation
  invalid_org = get_organisation(gh_instance, 'non_valid_org_username')
  assert get_members(invalid_org) is None

def test_get_repos() -> None:
  # Given a valid organisation
  assert get_repos(org) == repos
  # Given an invalid organisation
  invalid_org = get_organisation(gh_instance, 'non_valid_org_username')
  assert get_repos(invalid_org) is None

def test_validate_co_history_file() -> None:
  # Given a valid co_history file
  assert validate_co_history_file(co_history_file) == co_history_file_contents
  # Given a valid json file but invalid co_history file
  assert validate_co_history_file(valid_json_file) == None
  # Given a invalid json
  assert validate_co_history_file(invalid_json_file) == None