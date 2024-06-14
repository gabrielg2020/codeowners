import pytest
from modules.shuffler import (
  add_members_to_developers,
  backtrack
)

def test_add_members_to_developers(valid_members, valid_unfinished_developers, valid_developers) -> None:
  """Test add_members_to_developers with all valid inputs"""
  assert add_members_to_developers(valid_members, valid_unfinished_developers) == valid_developers

def test_add_members_to_developers_with_no_new_members(valid_unfinished_developers) -> None:
  """Test add_members_to_developers with no new members to add to developers"""
  assert add_members_to_developers([], valid_unfinished_developers) == valid_unfinished_developers
  
def test_add_members_to_developers_with_invalid_input() -> None:
  """Test add_members_to_developers with all invalid inputs"""
  assert add_members_to_developers('invalid_members', 'invalid_developers') is None

def test_backtrack(valid_developers, valid_repo_availability) -> None:
  distribution = []
  unassigned = []

  result = backtrack(valid_developers, valid_repo_availability, 0, distribution, unassigned)

  assert result is True
  assert len(unassigned) == 0
  assert len(distribution) == len(valid_developers) - len(unassigned)

def test_backtrack_with_no_developers(valid_repo_availability) -> None:
  empty_developers = []
  distribution = []
  unassigned = []

  result = backtrack(empty_developers, valid_repo_availability, 0, distribution, unassigned)

  assert result is True
  assert len(unassigned) == 0
  assert len(distribution) == len(empty_developers) - len(unassigned)

def test_backtrack_with_extra_developers(valid_developers, valid_repo_availability) -> None:
  valid_developers.append(
    {'acc_name': 'member_4', 'number_of_times_co': 0, 'current_repo': '', 'repos': []}
  )
  distribution = []
  unassigned = []

  result = backtrack(valid_developers, valid_repo_availability, 0, distribution, unassigned)

  assert result is True
  assert len(unassigned) == 1
  assert len(distribution) == len(valid_developers) - len(unassigned)

def test_backtrack_with_no_repos(valid_developers) -> None:
  repo_availability = {
    'repo_1': False,  
    'repo_2': False,
    'repo_3': False,
  }

  distribution = []
  unassigned = []

  result = backtrack(valid_developers, repo_availability, 0, distribution, unassigned)

  assert result is True
  assert len(unassigned) == 3
  assert len(distribution) == len(valid_developers) - len(unassigned)
