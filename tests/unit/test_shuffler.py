import pytest
from modules.shuffler import add_members_to_developers, get_new_repo

# --- Valid Variables ---
valid_members = ['test_acc_2', 'test_acc_3']

valid_developers = [
  {'acc_name':'test_acc_1',
    'number_of_times_co': 3,
    'current_repo': 'test_repo_1',
    'repos': [
      'testing_repo_2',
      'testing_repo_3'
    ]
  }
]

# --- Valid Returns ---
valid_add_members_to_developers_return = [
  {'acc_name':'test_acc_1',
    'number_of_times_co': 3,
    'current_repo': 'test_repo_1',
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