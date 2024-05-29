from github import Github, GithubException

def validate_api_key(key: str) -> Github | None:
  g = Github(key)
  try:
    # get_user().login will fail if bad credentials  
    g.get_user().login
    return g
  except GithubException as e:
    print(f"Failed to authenticate: {e.data['message']}")
    return None