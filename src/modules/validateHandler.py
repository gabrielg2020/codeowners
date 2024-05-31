from github import Github, GithubException, Auth
from github.Organization import Organization
from github.Repository import Repository
from github.ContentFile import ContentFile

def validate_api_token(token: str) -> Github | None:
  auth = Auth.Token(token)
  g = Github(auth=auth)
  try:
    g.get_user().login # Will fail if bad credentials  
    return g
  except GithubException as e:
    print(f"Failed to authenticate: {e.data['message']}")
    return None

def validate_org_username(g: Github, username: str) -> Organization | None:
  try:
    org = g.get_organization(username)
    return org
  except GithubException as e:
    print(f"Failed to find organisation: {e.data['message']}")
    return None

def validate_github_repo(org: Organization) -> Repository | None:
  try:
    repo = org.get_repo(".github")
    return repo
  except GithubException as e:
    print(f"Failed to find .github repo: {e.data['message']}")
    return None
  
def validate_file(r: Repository, file_name: str) -> list[ContentFile] | ContentFile | None:
  try:
    file = r.get_contents(file_name)
    return file
  except GithubException as e:
    print(f'Failed to find CODEOWNERS file: {e.data['message']}')
    return None
