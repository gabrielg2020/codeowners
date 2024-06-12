import pytest
import json
from modules.apiHandler import (
  get_codeowners_history_file,
  get_file,
  get_members,
  get_repos,
  validate_co_history_file,
  initialise_api
)

# --- get_github_instance ---
def test_get_github_instance_valid_token(valid_github) -> None:
  """Test GitHub authentication with valid token"""
  assert valid_github is not None

def test_get_github_instance_invalid_token(invalid_github) -> None:
  """Test GitHub authentication with invalid token"""
  assert invalid_github is None

# --- get_organisation ---
def test_get_organisation_valid_github_valid_name(valid_organisation) -> None:
  """Test organisation grabbing with valid Github & valid organisation name"""
  assert valid_organisation is not None

def test_get_organisation_valid_github_invalid_name(invalid_organisation) -> None:
  """Test organisation grabbing with valid Github & invalid organisation name"""
  assert invalid_organisation is None

def test_get_organisation_invalid_github_valid_name(invalid_organisation_invalid_github_valid_name) -> None:
  """Test organisation grabbing with invalid Github & valid organisation name"""
  assert invalid_organisation_invalid_github_valid_name is None

def test_get_organisation_invalid_github_invalid_name(invalid_organisation_invalid_github_invalid_name) -> None:
  """Test organisation grabbing with invalid Github & invalid organisation name"""
  assert invalid_organisation_invalid_github_invalid_name is None

# --- get_repo ---
def test_get_repo_valid_organisation_valid_repo_name(valid_repo) -> None:
  """Test repo grabbing with valid Organisation & valid repo name"""
  assert valid_repo is not None

def test_get_repo_valid_organisation_invalid_repo_name(invalid_repo) -> None:
  """Test repo grabbing with valid Organisation & invalid repo name"""
  assert invalid_repo is None

def test_get_repo_invalid_organisation_valid_repo_name(invalid_repo_invalid_org_valid_name) -> None:
  """Test repo grabbing with invalid Organisation & valid repo name"""
  assert invalid_repo_invalid_org_valid_name is None

def test_get_repo_invalid_organisation_invalid_repo_name(invalid_repo_invalid_org_invalid_name) -> None:
  """Test repo grabbing with invalid Organisation & invalid repo name"""
  assert invalid_repo_invalid_org_invalid_name is None

# --- get_members ---
def test_get_members_valid_organisation(valid_organisation) -> None:
  """Test members grabbing with valid Organisation"""
  assert get_members(valid_organisation) is not None

def test_get_members_invalid_organisation(invalid_organisation) -> None:
  """Test members grabbing with invalid Organisation"""
  assert get_members(invalid_organisation) is None

# --- get_repos ---
def test_get_repos_valid_organisation(valid_organisation) -> None:
  """Test repos grabbing with valid Organisation"""
  assert get_repos(valid_organisation) is not None

def test_get_repos_invalid_organisation(invalid_organisation) -> None:
  """Test repos grabbing with invalid Organisation"""
  assert get_repos(invalid_organisation) is None

# --- get_file ---
def test_get_file_valid_repository_valid_name(valid_repo) -> None:
  """Test file grabbing with valid Repository & valid name"""
  valid_file_name = 'test_file'
  assert get_file(valid_repo, valid_file_name) is not None

def test_get_file_valid_repository_invalid_name(valid_repo) -> None:
  """Test file grabbing with valid Repository & invalid name"""
  invalid_file_name = 'invalid_file_name'
  assert get_file(valid_repo, invalid_file_name) is None

def test_get_file_invalid_repository_valid_name(invalid_repo) -> None:
  """Test file grabbing with invalid Repository & valid name"""
  valid_file_name = 'test_file'
  assert get_file(invalid_repo, valid_file_name) is None

def test_get_file_invalid_repository_invalid_name(invalid_repo) -> None:
  """Test file grabbing with invalid Repository & invalid name"""
  invalid_file_name = 'invalid_file_name'
  assert get_file(invalid_repo, invalid_file_name) is None

def test_get_file_valid_repository_valid_dir_name(valid_repo) -> None:
  """Test file grabbing with valid Repository & valid directory name"""
  valid_dir_name = 'test-dir'
  assert get_file(valid_repo, valid_dir_name) is None

def test_get_file_invalid_repository_valid_dir_name(invalid_repo) -> None:
  """Test file grabbing with invalid Repository & valid directory name"""
  valid_dir_name = 'test-dir'
  assert get_file(invalid_repo, valid_dir_name) is None

# --- get_codeowners_history_file ---
def test_get_codeowners_history_file_valid_repository_co_valid_name(valid_repo) -> None:
  """Test codeowners-history grabbing with valid Repository & valid codeowners history name"""
  valid_file_name = 'valid_co_history.json'
  assert get_codeowners_history_file(valid_repo, valid_file_name) is not None

def test_get_codeowners_history_file_valid_repository_invalid_name(valid_repo) -> None:
  """Test codeowners-history grabbing with valid Repository & invalid name"""
  invalid_file_name = 'invalid_file_name'
  assert get_codeowners_history_file(valid_repo, invalid_file_name) == {'developers': []}

def test_get_codeowners_history_file_invalid_repository_co_valid_name(invalid_repo) -> None:
  """Test codeowners-history grabbing with invalid Repository & valid codeowners history name"""
  valid_file_name = 'valid_co_history.json'
  assert get_codeowners_history_file(invalid_repo, valid_file_name) is None

def test_get_codeowners_history_file_invalid_repository_invalid_name(invalid_repo) -> None:
  """Test codeowners-history grabbing with invalid Repository & invalid name"""
  invalid_file_name = 'invalid_file_name'
  assert get_codeowners_history_file(invalid_repo, invalid_file_name) is None

def test_get_codeowners_history_file_valid_repository_invalid_co_names(valid_repo) -> None:
  """Test codeowners-history grabbing with valid Repository & invalid codeowners history file names"""
  invalid_co_names = ['invalid_key_co_history.json', 'invalid_type_co_history.json', 'invalid_list_co_history.json']
  for invalid_co_name in invalid_co_names:
    assert get_codeowners_history_file(valid_repo, invalid_co_name) is None

def test_get_codeowners_history_file_invalid_repository_invalid_co_names(invalid_repo) -> None:
  """Test codeowners-history grabbing with invalid Repository & invalid codeowners history file names"""
  invalid_co_names = ['invalid_key_co_history.json', 'invalid_type_co_history.json', 'invalid_list_co_history.json']
  for invalid_co_name in invalid_co_names:
    assert get_codeowners_history_file(invalid_repo, invalid_co_name) is None

# --- validate_co_history_file ---
def test_validate_co_history_file_valid_json_valid_formatting() -> None:
  """Test validate_co_history_file with a valid json file with valid co_history formatting"""
  valid_co_history = {'developers': [
    {'acc_name': 'testing_acc',
    'number_of_times_co': 2,
    'current_repo': 'testing_current_repo',
    'repos': ['testing_repo_1']
    }
  ]}

  assert validate_co_history_file(json.dumps(valid_co_history)) == valid_co_history

def test_validate_co_history_file_invalid_json() -> None:
  """Test validate_co_history_file with an invalid json file"""
  invalid_json = 'invalid_json'

  assert validate_co_history_file(invalid_json) is None

def test_validate_co_history_file_valid_json_no_dev_list() -> None:
  """Test validate_co_history_file with an valid json file but no developers list"""
  invalid_co_history= {
    'acc_name': 'testing_acc',
    'number_of_times_co': 2,
    'current_repo': 'testing_current_repo',
    'repos': ['testing_repo_1']
    }
  
  assert validate_co_history_file(json.dumps(invalid_co_history)) is None

def test_validate_co_history_file_valid_json_no_acc_name() -> None:
  """Test validate_co_history_file with an valid json file but no acc_name attribute"""
  invalid_co_history = {'developers': [
    {'number_of_times_co': 2,
    'current_repo': 'testing_current_repo',
    'repos': ['testing_repo_1']
    }
  ]}
  
  assert validate_co_history_file(json.dumps(invalid_co_history)) is None

def test_validate_co_history_file_valid_json_no_number_of_times_co() -> None:
  """Test validate_co_history_file with an valid json file but no number_of_times_co attribute"""
  invalid_co_history = {'developers': [
    {'acc_name': 'testing_acc',
    'current_repo': 'testing_current_repo',
    'repos': ['testing_repo_1']
    }
  ]}
  
  assert validate_co_history_file(json.dumps(invalid_co_history)) is None

def test_validate_co_history_file_valid_json_no_current_repo() -> None:
  """Test validate_co_history_file with an valid json file but no current_repo attribute"""
  invalid_co_history = {'developers': [
    {'acc_name': 'testing_acc',
    'number_of_times_co': 2,
    'repos': ['testing_repo_1']
    }
  ]}
  
  assert validate_co_history_file(json.dumps(invalid_co_history)) is None

def test_validate_co_history_file_valid_json_no_repos() -> None:
  """Test validate_co_history_file with an valid json file but no repos attribute"""
  invalid_co_history = {'developers': [
    {'acc_name': 'testing_acc',
    'number_of_times_co': 2,
    'current_repo': 'testing_current_repo',
    }
  ]}
  
  assert validate_co_history_file(json.dumps(invalid_co_history)) is None

def test_validate_co_history_file_valid_json_invalid_acc_name_type() -> None:
  """Test validate_co_history_file with a valid json file with invalid acc_name type"""
  invalid_co_history = {'developers': [
    {'acc_name': 1234,
    'number_of_times_co': 2,
    'current_repo': 'testing_current_repo',
    'repos': ['testing_repo_1']
    }
  ]}

  assert validate_co_history_file(json.dumps(invalid_co_history)) is None

def test_validate_co_history_file_valid_json_invalid_number_of_times_co_type() -> None:
  """Test validate_co_history_file with a valid json file with invalid number_of_times_co type"""
  invalid_co_history = {'developers': [
    {'acc_name': 'testing_acc',
    'number_of_times_co': '1234',
    'current_repo': 'testing_current_repo',
    'repos': ['testing_repo_1']
    }
  ]}

  assert validate_co_history_file(json.dumps(invalid_co_history)) is None

def test_validate_co_history_file_valid_json_invalid_current_repo_type() -> None:
  """Test validate_co_history_file with a valid json file with invalid current_repo type"""
  invalid_co_history = {'developers': [
    {'acc_name': 'testing_acc',
    'number_of_times_co': 2,
    'current_repo': 1234,
    'repos': ['testing_repo_1']
    }
  ]}

  assert validate_co_history_file(json.dumps(invalid_co_history)) is None

def test_validate_co_history_file_valid_json_invalid_repos_type() -> None:
  """Test validate_co_history_file with a valid json file with invalid repos type"""
  invalid_co_history = {'developers': [
    {'acc_name': 'testing_acc',
    'number_of_times_co': 2,
    'current_repo': 'testing_current_repo',
    'repos': 1234
    }
  ]}

  assert validate_co_history_file(json.dumps(invalid_co_history)) is None

def test_validate_co_history_file_valid_json_invalid_repos_list_items_type() -> None:
  """Test validate_co_history_file with a valid json file with invalid repos list items type"""
  invalid_co_history = {'developers': [
    {'acc_name': 'testing_acc',
    'number_of_times_co': 2,
    'current_repo': 'testing_current_repo',
    'repos': ['string', 123, {'type': 'dict'}]
    }
  ]}

  assert validate_co_history_file(json.dumps(invalid_co_history)) is None

def test_initialise_api_valid() -> None:
  """Testing initialise_api with valid inputs"""
  valid_token = str(os.getenv('GH_API_TOKEN'))
  valid_org_name = 'codeowners-rfc-test'
  valid_repo_name = 'testing-repo'

  assert initialise_api(valid_token, valid_org_name, valid_repo_name) is not None

def test_initialise_api_invalid() -> None:
  """Testing initialise_api with invalid inputs"""
  invalid_token = 'invalid_token'
  invalid_org_name = 'invalid_org_name'
  invalid_repo_name = 'invalid_repo_name'

  assert initialise_api(invalid_token, invalid_org_name, invalid_repo_name) is None