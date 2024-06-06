import json
import logging
from github import Github, GithubException, Auth
from github.Organization import Organization
from github.Repository import Repository
from github.ContentFile import ContentFile

# Setting up logging package
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialise_api(token:str, org_name:str, repo_name:str) -> tuple[Github | None, Organization | None, Repository | None] | None:
  """Initialises GitHub API and returns instances of GitHub, Organisation and Repository."""
  g = get_github_instance(token)
  if g is None:
    return None
  org = get_organisation(g, org_name)
  if org is None:
    return None
  # Check .github repo
  repo = get_repo(org, repo_name)
  if repo is None:
    return None

  return g, org, repo

def get_codeowners_history_file(r: Repository, file_name: str = 'co_history.json') -> dict | None:
  """Returns the contents of the co_history.json file"""
  try:
    if r is None:
      logger.error('Repository inputted is None')
      return None

    # Check if file exists
    file_contents = get_file(r, file_name)
    if file_contents is None:
      logger.info(f'Cannot find {file_name}, creating a base history file.')
      return {'developers': []}
    
    # Validate file
    codeowners_content = validate_co_history_file(file_contents)
    return codeowners_content

  except GithubException as e:
    logger.error(f'Error encountered: {e.data['message']}')
    return None
  except Exception as e:
    logger.error(f'Exception has occurred: {e}')
    return None

def get_github_instance(token: str) -> Github | None:
  """Returns a GitHub instance if token is valid, else None."""
  auth = Auth.Token(token)
  g = Github(auth=auth)
  try:
    g.get_user().login # Will fail if bad credentials  
    return g
  except GithubException as e:
    logger.error(f'Failed to authenticate: {e.data['message']}')
    return None

def get_organisation(g: Github, org_name: str) -> Organization | None:
  """Returns a Organisation instance if org_name is valid, else None."""
  try:
    org = g.get_organization(org_name)
    return org
  except GithubException as e:
    logger.error(f'Failed to find organisation: {e.data['message']}')
    return None
  except Exception as e:
    logger.error(f'Exception has occurred: {e}')
    return None

def get_repo(org: Organization, repo_name: str) -> Repository | None:
  """Returns a Repository instance if repo_name is valid, else None."""
  try:
    repo = org.get_repo(repo_name)
    return repo
  except GithubException as e:
    logger.error(f'Failed to find .github repo: {e.data['message']}')
    return None
  except Exception as e:
    logger.error(f'Exception has occurred: {e}')
    return None
  
def get_file(r: Repository, file_name: str) -> list[ContentFile] | ContentFile | None:
  """Returns a ContentFile instance if file_name is valid, else None."""
  try:
    file = r.get_contents(file_name)
    # Check if file_name is the name of a directory
    if isinstance(file, list):
      logger.info(f'{file_name} is a directory not a file.')
      return None
    
    return file
  except GithubException as e:
    logger.error(f'Failed to find file: {e.data['message']}')
    return None
  except Exception as e:
    logger.error(f'Exception has occurred: {e}')
    return None
  
def get_members(o: Organization) ->  list[str] | None:
  """Returns a tuple of members if Organisation is valid, else None."""
  try:
    members = o.get_members()
    member_logins = list(member.login for member in members)
    return member_logins
  except GithubException as e:
    logger.error(f'Failed to get members: {e.data['message']}')
    return None
  except Exception as e:
    logger.error(f'Exception has occurred: {e}')
    return None

def get_repos(o: Organization) ->  list[str] | None:
  """Returns a tuple of repositories if Organisation is valid, else None."""
  try:
    repos = o.get_repos()
    # Make sure the .github repo is not added into the tuple
    repo_names = list(repo.name for repo in repos if repo.name != '.github')
    return repo_names
  except GithubException as e:
    logger.error(f'Failed to get repos: {e.data['message']}')
    return None
  except Exception as e:
    logger.error(f'Exception has occurred: {e}')
    return None
  
def validate_co_history_file(file_contents) -> dict:
  try:
    # Check if file follows .json formatting
    try:
      codeowners_content = file_contents.decoded_content.decode("utf-8")
      codeowners_content = json.loads(codeowners_content)
    except Exception as e:
      logger.error(f'Failed to decode into json, make sure that file is utf-8 encoded and in correct json format: {e.data['message']}')
      return None
    
    if 'developers' not in codeowners_content or not isinstance(codeowners_content['developers'], list):
      logger.error(f'.json does not have a "developers" list')
      return None
    
    # Check if file follows co_history.json formatting
    required_keys_types = {
      'acc_name': str,
      'number_of_times_co': int, 
      'current_repo': str,
      'repos': list
    }

    for developer in codeowners_content['developers']:
      # Check if keys are present
      if not all(key in developer for key in required_keys_types):
        logger.error(f'"developers" does not have the correct keys.')
        return None
      
      # Check if keys have correct type
      for key, expected_type in required_keys_types.items():
        if not isinstance(developer[key], expected_type):
          logger.error(f'"developers" keys does not have the correct types.')
          return None
        # Check that repos list is strings
        if key == 'repos' and not all(isinstance(item, str) for item in developer[key]):
          logger.error(f'"developers" "repos" list is not fully populated with string types.')
          return None
      
    return codeowners_content
  except GithubException as e:
    logger.error(f'Failed to get repos: {e.data['message']}')
    return None
  except Exception as e:
    logger.error(f'Exception has occurred: {e}')
    return None