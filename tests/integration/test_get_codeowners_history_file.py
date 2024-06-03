import os
import pytest
from modules.apiHandler import get_codeowners_history_file, get_github_instance, get_organisation, get_repo, get_file

# --- Valid Variables ---
token = str(os.getenv('GH_API_TOKEN'))
gh_instance = get_github_instance(token)
org = get_organisation(gh_instance, 'codeowners-rfc-test')
valid_repo = get_repo(org, 'testing-repo')
valid_json_name = 'valid.json'

# --- Valid Returns ---
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

# --- Invalid Variables ---
invalid_repo = get_repo(org, 'invalid_repo_name')
invalid_json_name = 'invalid.json'

def test_get_codeowners_history_file_with_invalid_repo() -> None:
  # file_name defaults to co_history.json
  # Given an invalid instance of Repository 
  assert get_codeowners_history_file(invalid_repo) is None
  # Given a non instance of Repository 
  assert get_codeowners_history_file("not_a_repository_instance") is None

def test_get_codeowners_history_file_with_valid_repo() -> None:
  # file_name defaults to co_history.json
  # Given a valid instance of Repository 
  assert get_codeowners_history_file(valid_repo) is None

def test_get_codeowners_history_file_with_invalid_json() -> None:
  # Given a valid instance of Repository with an invalid json file
  assert get_codeowners_history_file(valid_repo, invalid_json_name) is None

def test_get_codeowners_history_file_with_valid_json() -> None:
  # Given a valid instance of Repository with a valid json file but none valid co_history format
  assert get_codeowners_history_file(valid_repo, valid_json_name) is None

def test_get_codeowners_history_file_with_invalid_key_co_history() -> None:
  # Given a valid instance of Repository with a valid json file but none valid co_history format due to invalid key
  assert get_codeowners_history_file(valid_repo, 'invalid_key_co_history.json') is None

def test_get_codeowners_history_file_with_invalid_type_co_history() -> None:
  # Given a valid instance of Repository with a valid json file but none valid co_history format due to invalid type
  assert get_codeowners_history_file(valid_repo, 'invalid_key_co_history.json') is None

def test_get_codeowners_history_file_with_invalid_list_co_history() -> None:
  # Given a valid instance of Repository with a valid json file but none valid co_history format due to invalid "repos" list
  assert get_codeowners_history_file(valid_repo, 'invalid_key_co_history.json') is None