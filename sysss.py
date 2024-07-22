import requests
import sys
import json
if len(sys.argv)!=2:
    sys.exit()
else:
    x=requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+sys.argv[1])
o=x.json()
for i in o["results"]:
    print(i["trackName"])