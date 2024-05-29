import os
import pytest
from github import Github
from modules import validate_api_key

key = str(os.getenv("GH_API_KEY"))

def test_validate_api_key() -> None:
  # Given a valid API key
  assert validate_api_key(key).get_user().login == Github(key).get_user().login # type: ignore
  # Given an invalid API key
  assert validate_api_key('None_Valid_API_Key') == None

