import os
from github import Github
from dotenv import load_dotenv
from modules import validate_api_token, validate_org_username, validate_github_repo, validate_file

def main() -> None:
  # Load .env values
  load_dotenv()
  token = str(os.getenv("GH_API_TOKEN"))
  org_username = str(os.getenv("org_username"))

  # Check GitHub token
  g = validate_api_token(token)
  if g == None:
    return
  
  # Check Organisation name
  org = validate_org_username(g, org_username)
  if org == None:
    return
  
  # Check .github repo
  repo = validate_github_repo(org, 'testing-repo')
  if repo == None:
    return
  
  # Check CODEOWNERS file
  codeowners = validate_file(repo, 'test-file')
  if codeowners == None:
    return

if __name__ == "__main__":
  main()