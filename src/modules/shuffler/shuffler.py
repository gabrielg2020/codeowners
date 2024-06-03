import random

def shuffle_members(members: list, repos: list) -> dict[str, list]:
  co_history = {"developers":[]}
  for member in members:
    # Pick repo
    repo = random.choice(repos)
    repos.remove(repo)
    # Create json
    developer = {
      "acc_name": member,
      "number_of_times_co": 1,
      "repos": [repo]
    }
    co_history["developers"].append(developer)

  return co_history

