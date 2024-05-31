import os
from github import Github
from dotenv import load_dotenv
from modules import initialise_api, get_codeowners_history_file, get_file

def main() -> None:
  # Load .env values
  load_dotenv()
  token = str(os.getenv("GH_API_TOKEN"))
  org_username = "codeowners-rfc-test"
  repo_name = ".github"

  initialise_result = initialise_api(token, org_username, repo_name)
  if initialise_result is None:
    print("Initalisation failed. Please check your token, organisation name, or repository name")
    return
  
  g, org, repo = initialise_result

  print(get_codeowners_history_file(repo))

if __name__ == "__main__":
  main()