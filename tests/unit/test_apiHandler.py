import pytest
from modules.apiHandler import (
  get_codeowners_history_file,
  get_file,
  get_members,
  get_repos, 
  get_repo,
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
def test_get_organisation_valid_name(valid_organisation) -> None:
  """Test organisation grabbing with valid github & valid organisation name"""
  assert valid_organisation is not None

def test_get_organisation_valid_github_invalid_name(invalid_organisation) -> None:
  """Test organisation grabbing with valid github & invalid organisation name"""
  assert invalid_organisation is None

def test_get_organisation_invalid_github_valid_name(invalid_organisation_invalid_github_valid_name) -> None:
  """Test organisation grabbing with invalid github & valid organisation name"""
  assert invalid_organisation_invalid_github_valid_name is None

def test_get_organisation_invalid_github_invalid_name(invalid_organisation_invalid_github_invalid_name) -> None:
  """Test organisation grabbing with invalid github & invalid organisation name"""
  assert invalid_organisation_invalid_github_invalid_name is None

# --- get_repos ---
def test_get_repos_valid_organisation(valid_organisation) -> None:
  """Test repos grabbing with valid organisation"""
  assert get_repos(valid_organisation) is not None

def test_get_repos_invalid_organisation(invalid_organisation) -> None:
  """Test repos grabbing with invalid organisation"""
  assert get_repos(invalid_organisation) is None

# --- get_repo ---
def test_get_repo_valid_organisation_valid_repo_name(valid_organisation) -> None:
  """Test repo grabbing with valid organisation & valid repo name"""
  assert get_repo(valid_organisation, 'testing-repo') is not None

def test_get_repo_valid_organisation_invalid_repo_name(valid_organisation) -> None:
  """Test repo grabbing with valid organisation & invalid repo name"""
  assert get_repo(valid_organisation, 'invalid_repo_name') is None

def test_get_repo_invalid_organisation_valid_repo_name(invalid_organisation) -> None:
  """Test repo grabbing with invalid organisation & valid repo name"""
  assert get_repo(invalid_organisation, 'testing-repo') is None

def test_get_repo_invalid_organisation_invalid_repo_name(invalid_organisation) -> None:
  """Test repo grabbing with invalid organisation & invalid repo name"""
  assert get_repo(invalid_organisation, 'invalid_repo_name') is None


