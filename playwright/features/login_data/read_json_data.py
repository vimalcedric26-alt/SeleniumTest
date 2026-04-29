import json

file_path = '/playwright/features/login_data/credential.json'
with open(file=file_path,mode='r') as json_file:
    data = json.load(json_file)
    usernam = data[0]["username"]
    pwd = data[0]["password"]
