import pytest
from modules.shuffler import (
  add_members_to_developers
)

def test_add_members_to_developers_with_valid_members_valid_developers() -> None:
  """Test add_members_to_developers with valid members and valid developers"""
  valid_members = ['test_acc_1', 'test_acc_2']
  valid_developers = [{'acc_name': 'test_acc_1',
      'number_of_times_co': 1,
      'current_repo': 'current-repo',
      'repos': ['current-repo']}]
  
  valid_return =[{'acc_name': 'test_acc_1',
      'number_of_times_co': 1,
      'current_repo': 'current-repo',
      'repos': ['current-repo']},
      {'acc_name': 'test_acc_2',
      'number_of_times_co': 0,
      'current_repo': '',
      'repos': []}]
  
  assert add_members_to_developers(valid_members, valid_developers) == valid_return

def test_add_members_to_developers_with_invalid_members_valid_developers() -> None:
  """Test add_members_to_developers with invalid members and valid developers"""
  invalid_members = 'invalid_members'
  valid_developers = [{'acc_name': 'test_acc_1',
      'number_of_times_co': 1,
      'current_repo': 'current-repo',
      'repos': ['current-repo']}]
  
  assert add_members_to_developers(invalid_members, valid_developers) is None

def test_add_members_to_developers_with_valid_members_invalid_developers() -> None:
  """Test add_members_to_developers with valid members and invalid developers"""
  valid_members = ['test_acc_1', 'test_acc_2']
  invalid_developers = 'invalid_developers'
  
  assert add_members_to_developers(valid_members, invalid_developers) is None

def test_add_members_to_developers_with_invalid_members_invalid_developers() -> None:
  """Test add_members_to_developers with invalid members and invalid developers"""
  valid_members = ['test_acc_1', 'test_acc_2']
  invalid_developers = 'invalid_developers'
  
  assert add_members_to_developers(valid_members, invalid_developers) is None
