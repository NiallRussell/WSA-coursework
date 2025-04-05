import requests
from github import Github
from config import config as cfg

#Import API key from config file
api_key = cfg["private_api"]

#Authenticating connection to Github
g = Github(api_key)

#Get the repo
repo = g.get_repo("NiallRussell/aprivateone")

#Get the file
file = repo.get_contents("txt4ass4.txt", ref = "main")

#Decpde from bytes to string
file_content = file.decoded_content.decode("utf-8")

#Replace string
new_content = file_content.replace("Andrew", "Niall")

#Push changes
repo.update_file("txt4ass4.txt", "Replaced Andrew with Niall", new_content, file.sha)