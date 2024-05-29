import os
from github import Github
from dotenv import load_dotenv
from modules import validate_api_token, validate_org_repo

def main() -> None:
  # Load .env values
  load_dotenv()
  token = str(os.getenv("GH_API_TOKEN"))
  org_name = str(os.getenv("ORG_NAME"))

  # Check GitHub token
  g = validate_api_token(token)
  if g == None:
    return
  
  # Check Organisation
  repo = validate_org_repo(g, org_name)
  if repo == None:
    return

  print(repo)
if __name__ == "__main__":
  main()