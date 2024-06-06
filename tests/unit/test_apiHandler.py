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
  """Test repo grabbing with valid organisation & valid repo name"""
  assert valid_repo is not None

def test_get_repo_valid_organisation_invalid_repo_name(invalid_repo) -> None:
  """Test repo grabbing with valid organisation & invalid repo name"""
  assert invalid_repo is None

def test_get_repo_invalid_organisation_valid_repo_name(invalid_repo_invalid_org_valid_name) -> None:
  """Test repo grabbing with invalid organisation & valid repo name"""
  assert invalid_repo_invalid_org_valid_name is None

def test_get_repo_invalid_organisation_invalid_repo_name(invalid_repo_invalid_org_invalid_name) -> None:
  """Test repo grabbing with invalid organisation & invalid repo name"""
  assert invalid_repo_invalid_org_invalid_name is None

# --- get_repos ---
def test_get_repos_valid_organisation(valid_organisation) -> None:
  """Test repos grabbing with valid organisation"""
  assert get_repos(valid_organisation) is not None

def test_get_repos_invalid_organisation(invalid_organisation) -> None:
  """Test repos grabbing with invalid organisation"""
  assert get_repos(invalid_organisation) is None


