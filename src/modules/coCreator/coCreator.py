import logging
# Setting up logging package
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_codeowners_files(developers: dict, repos: list) -> dict:
  """Returns a repo_codeowners_map from a developer dictionary."""
  repo_developer_map = {}
  for developer in developers:
    current_repo = developer['current_repo']
    if current_repo in repo_developer_map:
      repo_developer_map[current_repo].append(developer['acc_name'])
    else:
      repo_developer_map[current_repo] = [developer['acc_name']]

  repo_codeowners_map = {}
  for repo in repos:
    codeowners_string = '# This file shows that '
    if repo in repo_developer_map:
      owners = repo_developer_map[repo]
      if owners:
        owners_str = " and ".join("@" + owner for owner in owners)
        codeowners_string += f'{owners_str} own the {repo} repository. \n * {" ".join("@" + owner for owner in owners)}'
      else:
        codeowners_string += f'nobody owns the {repo} repository. '
    else:
      codeowners_string += f'nobody owns the {repo} repository.'

    repo_codeowners_map[repo] = codeowners_string


  return repo_codeowners_map
