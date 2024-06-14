import pytest
from modules.shuffler import (
  add_members_to_developers,
  backtrack, 
  find_least_repeated_repo,
  get_developer_repo_distribution
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
  """Test backtrack with all valid inputs"""
  distribution = []
  unassigned = []

  result = backtrack(valid_developers, valid_repo_availability, 0, distribution, unassigned)

  assert result is True
  assert len(unassigned) == 0
  assert len(distribution) == len(valid_developers) - len(unassigned)

def test_backtrack_with_no_developers(valid_repo_availability) -> None:
  """Test backtrack with an empty developers list"""
  empty_developers = []
  distribution = []
  unassigned = []

  result = backtrack(empty_developers, valid_repo_availability, 0, distribution, unassigned)

  assert result is True
  assert len(unassigned) == 0
  assert len(distribution) == len(empty_developers) - len(unassigned)

def test_backtrack_with_extra_developers(valid_developers, valid_repo_availability) -> None:
  """Test backtrack with a developers list that is larger than repo dict"""
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
  """Test backtrack with an empty repos dict"""
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

def test_find_least_repeated_repo(valid_distribution) -> None:
  """Test find_least_repeated_repo with all valid inputs"""
  repos = ['repo_1', 'repo_2', 'repo_3']
  developer = {'acc_name': 'member_1', 'repos': ['repo_1', 'repo_2']}

  assert find_least_repeated_repo(developer, valid_distribution, repos) == 'repo_3'
  
def test_find_least_repeated_repo_with_empty_distribution() -> None:
  """Test find_least_repeated_repo with with empty distribution list"""
  distribution = []
  repos = ['repo_1', 'repo_2', 'repo_3']
  developer = {'acc_name': 'member_1', 'repos': ['repo_1']}

  assert find_least_repeated_repo(developer, distribution, repos) == 'repo_2'

def test_find_least_repeated_repo_with_full_developer_repos() -> None:
  """Test find_least_repeated_repo with with a developer that has all repos and empty developers list"""
  distribution = []
  repos = ['repo_1', 'repo_2', 'repo_3']
  developer = {'acc_name': 'member_1', 'repos': ['repo_1', 'repo_2', 'repo_3']}

  assert find_least_repeated_repo(developer, distribution, repos) is None

def test_get_developer_repo_distribution(valid_developers, valid_distribution) -> None:
  """Test get_developer_repo_distribution with all valid inputs"""
  repos = ['repo_1', 'repo_2', 'repo_3']
  
  assert get_developer_repo_distribution(valid_developers, repos) ==  valid_distribution

def test_get_developer_repo_distribution_with_all_repos_assigned() -> None:
  """Test get_developer_repo_distribution with developers having codeowned all repos"""
  developers = [
    {'acc_name': 'member_1', 'number_of_times_co': 3, 'current_repo': 'repo_1', 'repos': ['repo_1', 'repo_2', 'repo_3']},
    {'acc_name': 'member_2', 'number_of_times_co': 3, 'current_repo': 'repo_2', 'repos': ['repo_1', 'repo_2', 'repo_3']},
    {'acc_name': 'member_3', 'number_of_times_co': 3, 'current_repo': 'repo_3', 'repos': ['repo_1', 'repo_2', 'repo_2']},
  ]
  repos = ['repo_1', 'repo_2', 'repo_3']

  expected_result = [
    {'acc_name': 'member_3', 'new_repo': 'repo_3'}, 
    {'acc_name': 'member_1', 'new_repo': 'repo_1'}, 
    {'acc_name': 'member_2', 'new_repo': 'repo_2'}
  ]

  assert get_developer_repo_distribution(developers, repos) == expected_result
  
def test_get_developer_repo_distribution_with_all_repos_assigned() -> None:
  """Test get_developer_repo_distribution with more developers than repos and all developers having codeowned all repos"""
  developers = [
    {'acc_name': 'member_1', 'number_of_times_co': 3, 'current_repo': 'repo_1', 'repos': ['repo_1', 'repo_2', 'repo_3']},
    {'acc_name': 'member_2', 'number_of_times_co': 3, 'current_repo': 'repo_2', 'repos': ['repo_1', 'repo_2', 'repo_3']},
    {'acc_name': 'member_3', 'number_of_times_co': 3, 'current_repo': 'repo_3', 'repos': ['repo_1', 'repo_2', 'repo_2']},
    {'acc_name': 'member_4', 'number_of_times_co': 3, 'current_repo': 'repo_3', 'repos': ['repo_1', 'repo_2', 'repo_2']},
  ]
  repos = ['repo_1', 'repo_2', 'repo_3']

  expected_result = [
    {'acc_name': 'member_3', 'new_repo': 'repo_3'}, 
    {'acc_name': 'member_1', 'new_repo': 'repo_1'}, 
    {'acc_name': 'member_2', 'new_repo': 'repo_2'},
    {'acc_name': 'member_4', 'new_repo': 'repo_3'},
  ]

  assert get_developer_repo_distribution(developers, repos) == expected_result