import os
from github import Github
from dotenv import load_dotenv
from modules.validateHandler import validate_api_key

def main() -> None:
  load_dotenv()
  key = str(os.getenv("GH_API_KEY"))
  g = validate_api_key(key)

  if g == None:
    return

if __name__ == "__main__":
  main()