import os
from github import Github
from github.Organization import Organization
from github.Repository import Repository
import pytest
from modules.apiHandler import (
  get_github_instance,
  get_organisation,
  get_repo
)

# --- get_github_instance ---
@pytest.fixture
def valid_github() -> Github | None:
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
  """Fixture to provide an invalid Organisation with invalid Github"""
  valid_org_name = 'codeowners-rfc-test'
  org = get_organisation(invalid_github, valid_org_name)
  return org

@pytest.fixture
def invalid_organisation_invalid_github_invalid_name(invalid_github) -> Organization | None:
  """Fixture to provide an invalid Organisation with invalid Github & invalid name"""
  invalid_org_name = 'invalid_org_name'
  org = get_organisation(invalid_github, invalid_org_name)
  return org

# --- get_repo ---
@pytest.fixture
def valid_repo(valid_organisation)  -> Repository | None:
  """Fixture to provide a valid Repository"""
  valid_repo_name = 'testing-repo'
  repo = get_repo(valid_organisation, valid_repo_name)
  return repo

@pytest.fixture
def invalid_repo(valid_organisation)  -> Repository | None:
  """Fixture to provide an invalid Repository with invalid name"""
  invalid_repo_name = 'invalid_repo_name'
  repo = get_repo(valid_organisation, invalid_repo_name)
  return repo

@pytest.fixture
def invalid_repo_invalid_org_valid_name(invalid_organisation)  -> Repository | None:
  """Fixture to provide an invalid Repository with invalid Organisation """
  valid_repo_name = 'testing-repo'
  repo = get_repo(invalid_organisation, valid_repo_name)
  return repo

@pytest.fixture
def invalid_repo_invalid_org_invalid_name(invalid_organisation)  -> Repository | None:
  """Fixture to provide an invalid Repository with invalid Organisation & invalid name"""
  invalid_repo_name = 'invalid_repo_name'
  repo = get_repo(invalid_organisation, invalid_repo_name)
  return repo

# --- shuffle.py ---
@pytest.fixture
def valid_members() -> list[str]:
  return ['member_1', 'member_2', 'member_3']

@pytest.fixture
def valid_unfinished_developers() -> list[dict]:
  return [
    {'acc_name': 'member_1', 'number_of_times_co': 1, 'current_repo': 'current-repo', 'repos': ['repo_1']}
  ]

@pytest.fixture
def valid_developers() -> list[dict]:
  return [
    {'acc_name': 'member_1', 'number_of_times_co': 1, 'current_repo': 'current-repo', 'repos': ['repo_1']},
    {'acc_name': 'member_2', 'number_of_times_co': 0, 'current_repo': '', 'repos': []},
    {'acc_name': 'member_3', 'number_of_times_co': 0, 'current_repo': '', 'repos': []}
  ]

@pytest.fixture
def valid_repo_availability() -> dict:
  return {
    'repo_1': True,
    'repo_2': True,
    'repo_3': True
  }

@pytest.fixture
def valid_distribution() -> list[dict]:
  return [
    {'acc_name': 'member_2', 'new_repo': 'repo_1'},
    {'acc_name': 'member_3', 'new_repo': 'repo_2'},
    {'acc_name': 'member_1', 'new_repo': 'repo_3'}
  ]