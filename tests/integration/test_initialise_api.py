import pytest
import os
from modules.apiHandler import initialise_api

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