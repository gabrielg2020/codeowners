from github import Github, GithubException, Auth

def validate_api_key(key: str) -> Github | None:
  auth = Auth.Token(key)
  g = Github(auth=auth)
  try:
    # get_user().login will fail if bad credentials  
    g.get_user().login
    return g
  except GithubException as e:
    print(f"Failed to authenticate: {e.data['message']}")
    return None