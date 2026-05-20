import os

filename = "marketplace_db.json"
if os.path.exists(filename):
    print("File already exists!")

else:
    print("The file does not exist yet")