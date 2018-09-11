# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 19:35:11 2018

@author: wangj
"""

import requests

my_wm_username = 'jwang45'
search_url = 'http://buckets.peterbeshai.com/api/?player=201939&season=2015'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})


# Write your program here to populate the appropriate variables
JumpShotsAttempt = [(shot["ACTION_TYPE"], shot["EVENT_TYPE"]) for shot in response.json() if shot["ACTION_TYPE"] == "Jump Shot"]
JumpShotsMade = [madeshot for madeshot in JumpShotsAttempt if madeshot[1] == "Made Shot"]


percJumpShotMade = len(JumpShotsMade) / len(JumpShotsAttempt)


print(my_wm_username)
print(len(JumpShotsAttempt))
print(len(JumpShotsMade))
print(percJumpShotMade)
