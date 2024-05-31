import os
from github import Github
from dotenv import load_dotenv
from modules import get_github_instance, get_organisation, get_repo, get_file

def main() -> None:
  # Load .env values
  load_dotenv()
  token = str(os.getenv("GH_API_TOKEN"))
  org_username = str(os.getenv("org_username"))

  # Check GitHub token
  g = get_github_instance(token)
  if g == None:
    return
  
  # Check Organisation name
  org = get_organisation(g, org_username)
  if org == None:
    return
  
  # Check .github repo
  repo = get_repo(org, 'testing-repo')
  if repo == None:
    return
  
  # Check CODEOWNERS file
  codeowners = get_file(repo, 'test-file')
  if codeowners == None:
    return

if __name__ == "__main__":
  main()