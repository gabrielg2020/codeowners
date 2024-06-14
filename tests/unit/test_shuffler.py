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


