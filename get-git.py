#!/usr/bin/env python3
# Get git repo
  
import json
import subprocess
import sys

if len(sys.argv ) < 4:
    print('Usage: ./git-get.py [token] [owner] [repo]')
else:
    token = sys.argv[1]
    owner = sys.argv[2]
    repo = sys.argv[3]


    out = subprocess.run("""curl -H 'Authorization: token {}' https://api.github.com/repos/{}/{}/releases/latest""".format(token, owner, repo), shell=True, capture_output=True)
    out_json = json.loads(out.stdout)
    out_url = out_json['assets_url']

    assets = subprocess.run("""curl -H 'Authorization: token {}' {}""".format(token, out_url), shell=True, capture_output=True)
    assets_json = json.loads(assets.stdout)
    assets_url = assets_json[0]['url']

    print(assets_url)

    subprocess.run("""curl -vLJO -H 'Authorization: token {}' -H 'Accept: application/octet-stream' {}""".format(token, assets_url), shell=True)
