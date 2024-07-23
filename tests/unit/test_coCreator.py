import pytest
from modules.coCreator import (
  create_codeowners_files
)

def test_create_codeowners_files_valid_developer_valid_repos() -> None:
  valid_developers = [{
    'acc_name': 'dev_1',
    'current_repo': 'test_repo_1'
  },{
    'acc_name': 'dev_2',
    'current_repo': 'test_repo_2'
  }]

  valid_repos = ['test_repo_1', 'test_repo_2', 'test_repo_3']

  valid_return = {
    "test_repo_1": "# This file shows that @dev_1 own the test_repo_1 repository. \n * @dev_1",
    "test_repo_2": "# This file shows that @dev_2 own the test_repo_2 repository. \n * @dev_2",
    "test_repo_3": "# This file shows that nobody owns the test_repo_3 repository."
  }

  assert create_codeowners_files(valid_developers, valid_repos) == valid_return