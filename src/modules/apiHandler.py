from github import Github, GithubException, Auth
from github.Organization import Organization
from github.Repository import Repository
from github.ContentFile import ContentFile

def initialise_api(token:str, org_username:str, rep_name:str) -> tuple[Github | None, Organization | None, Repository | None] | None:
  g = get_github_instance(token)
  if g == None:
    return None
  org = get_organisation(g, org_username)
  if org == None:
    return None
  # Check .github repo
  repo = get_repo(org, 'testing-repo')
  if repo == None:
    return None

  return (g, org, repo)
def get_github_instance(token: str) -> Github | None:
  auth = Auth.Token(token)
  g = Github(auth=auth)
  try:
    g.get_user().login # Will fail if bad credentials  
    return g
  except GithubException as e:
    print(f"Failed to authenticate: {e.data['message']}")
    return None

def get_organisation(g: Github, username: str) -> Organization | None:
  try:
    org = g.get_organization(username)
    return org
  except GithubException as e:
    print(f"Failed to find organisation: {e.data['message']}")
    return None

def get_repo(org: Organization, repo_name: str) -> Repository | None:
  try:
    repo = org.get_repo(repo_name)
    return repo
  except GithubException as e:
    print(f"Failed to find .github repo: {e.data['message']}")
    return None
  
def get_file(r: Repository, file_name: str) -> list[ContentFile] | ContentFile | None:
  try:
    file = r.get_contents(file_name)
    return file
  except GithubException as e:
    print(f'Failed to find file: {e.data['message']}')
    return None
