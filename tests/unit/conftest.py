import os
from github import Github
from github.Organization import Organization
import pytest
from modules.apiHandler import (
  get_github_instance,
  get_organisation
)

# --- get_github_instance ---
@pytest.fixture
def valid_github():
  """Fixture to provide a valid Github instance"""
  valid_token = str(os.getenv('GH_API_TOKEN'))
  g = get_github_instance(valid_token)
  return g

@pytest.fixture
def invalid_github() -> Github | None:
  """Fixture to provide an invalid Github instance"""
  invalid_token = 'invalid_token'
  g = get_github_instance(invalid_token)
  return g

# --- get_organisation ---
@pytest.fixture
def valid_organisation(valid_github) -> Organization | None:
  """Fixture to provide a valid Organisation"""
  valid_org_name = 'codeowners-rfc-test'
  org = get_organisation(valid_github, valid_org_name)
  return org

@pytest.fixture
def invalid_organisation(valid_github) -> Organization | None:
  """Fixture to provide an invalid Organisation with invalid name"""
  invalid_org_name = 'invalid_org_name'
  org = get_organisation(valid_github, invalid_org_name)
  return org

@pytest.fixture
def invalid_organisation_invalid_github_valid_name(invalid_github) -> Organization | None:
  """Fixture to provide an invalid Organisation with invalid github"""
  valid_org_name = 'codeowners-rfc-test'
  org = get_organisation(invalid_github, valid_org_name)
  return org

@pytest.fixture
def invalid_organisation_invalid_github_invalid_name(invalid_github) -> Organization | None:
  """Fixture to provide an invalid Organisation with invalid github & invalid name"""
  invalid_org_name = 'invalid_org_name'
  org = get_organisation(invalid_github, invalid_org_name)
  return org