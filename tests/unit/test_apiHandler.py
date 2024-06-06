import pytest
from modules.apiHandler import (
  get_codeowners_history_file,
  get_github_instance, 
  get_organisation,
  get_file,
  get_members,
  get_repos, 
  get_repo,
  validate_co_history_file
)

# --- Mock Data ---

# --- Tests ---
def test_get_github_instance_valid_token(valid_github) -> None:
  """Test successful GitHub authentication"""
  assert valid_github is not None

def test_get_github_instance_invalid_token(invalid_github) -> None:
  """Test GitHub authentication with bad credentials"""
  assert invalid_github is None

def test_get_organisation_valid_name(valid_organisation) -> None:
  """Test successful organisation grabbing"""
  assert valid_organisation is not None

def test_get_organisation_invalid_name(invalid_organisation) -> None:
  """Test organisation grabbing with wrong organisation name"""
  assert invalid_organisation is None