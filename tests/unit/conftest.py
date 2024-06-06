import os
import pytest
from unittest.mock import patch
from github import Github, GithubException
from modules.apiHandler import get_github_instance

# --- Fixtures ---
@pytest.fixture
def mock_github_instance(mocker):
  """Fixture to mock Github class"""
  return mocker.patch('github.Github', autospec=True)

@pytest.fixture
def valid_github(mock_github_instance):
  """Fixture to provide a valid Github instance"""
  mock_github_instance.return_value.get_user.return_value.login = 'gabrielg2020'
  valid_token = str(os.getenv('GH_API_TOKEN'))
  g = get_github_instance(valid_token)
  return g

@pytest.fixture
def invalid_github(mock_github_instance):
  """Fixture to provide an invalid Github instance"""
  mock_github_instance.return_value.get_user.side_effect = GithubException(
    status=401,
    data={'message': 'Bad credentials'}
  )
  invalid_token = 'invalid_token'
  g = get_github_instance(invalid_token)
  return g