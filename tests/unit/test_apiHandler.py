import pytest
from modules.apiHandler import (
  get_codeowners_history_file,
  get_file,
  get_members,
  get_repos,
  validate_co_history_file
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