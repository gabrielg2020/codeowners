import random

def shuffle_members_current_repos(members: list, repos: list, developers: dict):
  """Changes all members current_repo, adds current_repo to repos list and increments number_of_times_co"""
  assigned_repos = set()
  
  # Add members that don't exist in developers
  developers = add_members_to_developers(members, developers)

  # Sort by the least amount of times as a co
  sorted_developers = sorted(developers, key=lambda dev: dev["number_of_times_co"])

  # Assign repos to developers
  for developer in sorted_developers:
    new_repo = get_new_repo(developer, repos, assigned_repos)

    if new_repo not in developer['repos']:
      # Only add repos that weren't there before
      developer['repos'].append(new_repo)
    developer['current_repo'] = new_repo
    developer['number_of_times_co'] += 1

  return sorted_developers

def add_members_to_developers(members: list, developers: list) -> list[dict]:
  """Returns a list of all members as developers"""
  for member in members:
    if not any(developer['acc_name'] == member for developer in developers):
      developers.append({
        "acc_name": member,
        "number_of_times_co": 0,
        "current_repo": '',
        "repos": []
      })

  return developers

def get_new_repo(developer: dict, all_repos: list, assigned_repos: set) -> str:
  """Returns a new_repo based of data in co_history"""
  # Removes repos from all_repos that are in developer['repos']
  available_repos = [repo for repo in all_repos if repo not in developer['repos']]
  if available_repos == []:
    # If there are no available repos pick from any of them
    assigned_repos.clear()
    available_repos = all_repos.copy()
    available_repos.remove(developer['current_repo'])

  new_repo = random.choice(available_repos)
  assigned_repos.add(new_repo)

  return new_repo