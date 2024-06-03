import pytest
from modules.shuffler import add_members_to_developers, get_new_repo

# --- Valid Variables ---
assigned_repos = set()

valid_members = ['test_acc_2', 'test_acc_3']

valid_developers = [
  {'acc_name':'test_acc_1',
    'number_of_times_co': 3,
    'current_repo': 'testing_repo_1',
    'repos': [
      'testing_repo_2',
      'testing_repo_3'
    ]
  }
]

valid_developer_for_get_new_repo = {
  'acc_name':'test_acc_1',
  'number_of_times_co': 2,
  'current_repo': 'testing_repo_1',
  'repos': [
    'testing_repo_2',
    'testing_repo_1'
  ]
}

valid_all_repos = ['testing_repo_1', 'testing_repo_2']

invalid_all_repos = ['invalid_repo_1', 'invalid_repo_2']
# --- Valid Returns ---
valid_add_members_to_developers_return = [
  {'acc_name':'test_acc_1',
    'number_of_times_co': 3,
    'current_repo': 'testing_repo_1',
    'repos': [
      'testing_repo_2',
      'testing_repo_3'
    ]
  },
  {'acc_name':'test_acc_2',
    'number_of_times_co': 0,
    'current_repo': '',
    'repos': []
  },
  {'acc_name':'test_acc_3',
    'number_of_times_co': 0,
    'current_repo': '',
    'repos': []
  }
]

def test_add_members_to_developers() -> None:
  # Given an invalid members list with a valid developers list
  assert add_members_to_developers('invalid_members', valid_developers) is None
  # Given a valid members list with an invalid developers list
  assert add_members_to_developers(valid_members, 'invalid_developers') is None
  # Given an invalid members list with an invalid developers list
  assert add_members_to_developers('invalid_members', 'invalid_developers') is None
  # Given a valid members list with a valid developers list
  assert add_members_to_developers(valid_members, valid_developers) == valid_add_members_to_developers_return

def test_get_new_repo() -> None:
  # Given a valid developer dict and an invalid all_repos list
  assert get_new_repo(valid_developer_for_get_new_repo, 'invalid_all_repos', assigned_repos) is None
  # Given an invalid developer dict and a valid all_repos list
  assert get_new_repo('invalid_developer', valid_all_repos, assigned_repos) is None
  # Given an invalid developer dict and an invalid all_repos list
  assert get_new_repo('invalid_developer', 'invalid_all_repos', assigned_repos) is None
  # Given a valid developer dict and a valid all_repos list
  assert get_new_repo(valid_developer_for_get_new_repo, valid_all_repos, assigned_repos) == 'testing_repo_2'