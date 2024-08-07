import os
import json
from dotenv import load_dotenv
from modules.apiHandler import initialise_api, get_codeowners_history_file, get_members, get_repos, write_to_file, get_repo
from modules.shuffler import shuffle_members_current_repos
from modules.coCreator import create_codeowners_files

class PrintColour:
  """Class which hold potential print colours"""
  red = '\033[31m'
  green = '\033[32m'


def main() -> None:
  """Main Function"""
  # Load .env values
  load_dotenv()
  token = str(os.getenv('GH_API_TOKEN'))
  org_username = 'codeowners-rfc-test'
  repo_name = '.github'

  # Initialise API
  initialise_result = initialise_api(token, org_username, repo_name)
  if initialise_result is None:
    print(PrintColour.red, 'Initalisation failed. Please check your token, organisation name, or repository name. \n')
    return

  org, repo = initialise_result

  print(PrintColour.green, f'API successfully connected to: {org_username}. \n')

  # Grab org details
  members = get_members(org)
  repos = get_repos(org)
  co_history = get_codeowners_history_file(repo, 'co_history.json')

  # Create and push new co_history.json
  new_developers = shuffle_members_current_repos(members, repos, co_history['developers'])
  new_co_history = json.dumps({
    "developers": new_developers
  })

  write_to_file('co_history.json', new_co_history, repo)

  # Create and push new CODEOWNERS
  repo_codeowners_map = create_codeowners_files(new_developers, repos)

  for repo, codeowners in repo_codeowners_map.items():
    current_repo = get_repo(org, repo)
    write_to_file('.github/CODEOWNERS', codeowners, current_repo)

  print(PrintColour.green, 'Successfully wrote to .github/co_history.json & <repo>/.github/CODEOWNERS \n')

  print(PrintColour.green, 'Successfully shuffled developers. \n')

if __name__ == '__main__':
  main()
