from github import Github, GithubException

def validate_api_key(key: str) -> Github | None:
  try:
    g = Github(key)
    return g
  except GithubException as e:
    print(f"Failed to authenticate: {e.data['message']}")
    return None