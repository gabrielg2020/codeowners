import logging

# Setting up logging package
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def shuffle_members_current_repos(members: list, repos: list, developers: list) -> list | None:
  """Changes all members current_repo, adds current_repo to repos list and increments number_of_times_co"""
  if not isinstance(members, list) or not isinstance(repos, list):
      logger.error("'members' or 'repos' are not type list")
      return None
  
  # Add members that don't exist in developers
  developers = add_members_to_developers(members, developers)
  if developers is None:
    return None

  distribution = get_developer_repo_distribution(developers, repos)

  # Update developers list
  for i in range(len(developers)):
    developers[i]['current_repo'] = distribution[i]['new_repo']
    developers[i]['repos'].append(distribution[i]['new_repo'])
    developers[i]['repos'] = list(set(developers[i]['repos']))
    developers[i]['number_of_times_co'] += 1

  return developers

def add_members_to_developers(members: list, developers: list) -> list[dict]:
  """Returns a list of all members as developers"""
  if not isinstance(members, list) or not isinstance(developers, list):
    logger.error("'members' or 'developers' are not type list")
    return None
  for member in members:
    if not any(developer['acc_name'] == member for developer in developers):
      developers.append({
        'acc_name': member,
        'number_of_times_co': 0,
        'current_repo': '',
        'repos': []
      })

  return developers

def get_developer_repo_distribution(developers: list, repos: list) -> list:
  """Returns the distribution based of data in developers and repos"""
  # Sort developers by the repos they previously had
  developers.sort(key=lambda dev: len(dev['repos']))
  
  # Availability map
  repo_availability = {repo: True for repo in repos}

  distribution = []
  unassigned = []

  # Start backtracking from the first dev
  backtrack(developers, repo_availability, 0, distribution, unassigned)

  # Assign any remaining repos to the unassigned developers
  for developer in unassigned:
    optimal_repo = find_least_repeated_repo(developer, distribution, repos)
    if optimal_repo:
      distribution.append({'acc_name': developer['acc_name'], 'new_repo': optimal_repo})
    else:
      # If no optimal repo is found (all repos are perviously assigned), assign any fruit with the least counts
      for repo in repos:
        if repo_availability[repo]:
          distribution.append({'acc_name': developer['acc_name'], 'new_repo': repo})
          break

  return distribution

def backtrack(developers: list, repo_availability: dict, index: int, distribution: list, unassigned: list) -> bool:
  """A recursive exploration algorithm. Returns a bool to determine if exploration is finished"""
  # Recursive base case
  if index == len(developers):
    return True
  
  developer = developers[index]
  assigned = False
  for repo in repo_availability:
    if repo_availability[repo] and is_valid_assignment(developer, repo):
      # Assign the repo to the developer
      distribution.append({'acc_name': developer['acc_name'], 'new_repo': repo})
      repo_availability[repo] = False
      assigned = True

      # Recursively assign repos to the remaining developers
      if backtrack(developers, repo_availability, index + 1, distribution, unassigned):
        return True
      
      # Backtrack if assignment was not successful
      distribution.pop()
      repo_availability[repo] = True
      assigned = False

  if not assigned:
    unassigned.append(developer)
    return backtrack(developers, repo_availability, index + 1, distribution, unassigned)

  return False

def is_valid_assignment(developer: dict, repo: str) -> bool:
  """Returns bool determining if a repo is valid for assignment"""
  return repo not in developer['repos']

def find_least_repeated_repo(developer: dict, distribution: list, repos: list) -> str | None:
  """Uses a 'greedy' approach. Returns the least repeated repository"""
  repo_count = {repo: 0 for repo in repos}
  for entry in distribution:
    repo_count[entry['new_repo']] += 1
  least_repeated_repo = None
  min_count = float('inf')
  for repo, count in repo_count.items():
    if repo not in developer['repos'] and count < min_count:
      least_repeated_repo = repo
      min_count = count

  return least_repeated_repo
