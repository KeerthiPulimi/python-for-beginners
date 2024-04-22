import requests
import sys
import json
def main():
  if len(sys.argv)!=2:
   print(":usage is pyhon")

    
    


if len(sys.argv)!= 2:
  sys.exit()

requests.get("https://itunes.apple.com/search?entity=song$limit=1&tem=")
print(json.dumps(response.json(), indent = 2))
