import os
from github import Github
from dotenv import load_dotenv
from modules.apiHandler import initialise_api, get_codeowners_history_file, get_members, get_repos
from modules.shuffler import shuffle_members_current_repos

def main() -> None:  
  # Load .env values
  load_dotenv()
  token = str(os.getenv('GH_API_TOKEN'))
  org_username = 'codeowners-rfc-test'
  repo_name = '.github'

  initialise_result = initialise_api(token, org_username, repo_name)
  if initialise_result is None:
    print('Initalisation failed. Please check your token, organisation name, or repository name')
    return
  
  g, org, repo = initialise_result

  members = get_members(org)
  repos = get_repos(org)
  co_history = get_codeowners_history_file(repo)

#   test = [{
#     'acc_name':'test_acc_1',
#     'number_of_times_co': 3,
#     'current_repo': 'testing_repo_1',
#     'repos': [
#       'testing_repo_1',
#       'testing_repo_2',
#       'testing_repo_3']
#   }, {
#     'acc_name':'test_acc_2',
#     'number_of_times_co': 2,
#     'current_repo': 'testing_repo_2',
#     'repos': [
#       'testing_repo_2',
#       'testing_repo_4']
#   }, {
#     'acc_name':'test_acc_3',
#     'number_of_times_co': 4,
#     'current_repo': 'testing_repo_3',
#     'repos': [
#       'testing_repo_1',
#       'testing_repo_2',
#       'testing_repo_3',
#       'testing_repo_4']
#   }, {
#     'acc_name':'test_acc_4',
#     'number_of_times_co': 1,
#     'current_repo': 'testing_repo_4',
#     'repos': [
#       'testing_repo_2']
#   }
# ]
  
#   repos = [
#     'testing_repo_1', 
#     'testing_repo_2',
#     'testing_repo_3',
#     'testing_repo_4'
#   ]

  shuffle_members_current_repos(members, repos, co_history['developers'])

if __name__ == '__main__':
  main()