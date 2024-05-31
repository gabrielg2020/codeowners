from github import Github, GithubException, Auth
from github.Organization import Organization
from github.Repository import Repository
from github.ContentFile import ContentFile

def initialise_api(token:str, org_name:str, repo_name:str) -> tuple[Github | None, Organization | None, Repository | None] | None:
  """Initialises GitHub API and returns instances of GitHub, Organisation and Repository."""
  g = get_github_instance(token)
  if g == None:
    return None
  org = get_organisation(g, org_name)
  if org == None:
    return None
  # Check .github repo
  repo = get_repo(org, repo_name)
  if repo == None:
    return None

  return g, org, repo

def get_github_instance(token: str) -> Github | None:
  """Returns a GitHub instance if token is valid, else None."""
  auth = Auth.Token(token)
  g = Github(auth=auth)
  try:
    g.get_user().login # Will fail if bad credentials  
    return g
  except GithubException as e:
    print(f"Failed to authenticate: {e.data['message']}")
    return None

def get_organisation(g: Github, org_name: str) -> Organization | None:
  """Returns a Organisation instance if org_name is valid, else None."""
  try:
    org = g.get_organization(org_name)
    return org
  except GithubException as e:
    print(f"Failed to find organisation: {e.data['message']}")
    return None

def get_repo(org: Organization, repo_name: str) -> Repository | None:
  """Returns a Repository instance if repo_name is valid, else None."""
  try:
    repo = org.get_repo(repo_name)
    return repo
  except GithubException as e:
    print(f"Failed to find .github repo: {e.data['message']}")
    return None
  
def get_file(r: Repository, file_name: str) -> list[ContentFile] | ContentFile | None:
  """Returns a ContentFile instance if file_name is valid, else None."""
  try:
    file = r.get_contents(file_name)
    return file
  except GithubException as e:
    print(f'Failed to find file: {e.data['message']}')
    return None
