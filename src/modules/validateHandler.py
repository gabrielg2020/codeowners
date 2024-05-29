from github import Github, GithubException, Auth
from github.Repository import Repository

def validate_api_token(token: str) -> Github | None:
  auth = Auth.Token(token)
  g = Github(auth=auth)
  try:
    g.get_user().login # Will fail if bad credentials  
    return g
  except GithubException as e:
    print(f"Failed to authenticate: {e.data['message']}")
    return None
  
def validate_org_repo(g:Github, name: str) -> Repository | None:
  org = g.get_organization(name)
  try:
    repo = org.get_repo(".github") # Will fail if bad credentials 
    return repo
  except GithubException as e:
    print(f"Failed to get organisation .github repo: {e.data['message']}")
    return None