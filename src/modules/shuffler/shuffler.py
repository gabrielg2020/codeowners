import random

def shuffle_members(members: list, repos: list, co_history: dict) -> dict[str, list]:
  developers = co_history["developers"]
  # Add members that don't exist in developers
  for member in members:
    if any(developer['acc_name'] == member for developer in developers):
        print(f"{member} exists in developers.")
    else:
      print(f'{member} doesnt exist in dev')
      developers.append({
        "acc_name": member,
        "number_of_times_co": 0,
        "repos": []
      })

  return developers

