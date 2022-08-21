import requests
import time
import json
import os
from requests.structures import CaseInsensitiveDict

url = "http://game.buffloft.com/tapStore/storeReward"
url2 = "http://game.buffloft.com/tapBigTurntable/sendReward"


spinitk=os.environ.get('spin_token')
rewardtoken=os.environ.get('reward_token')
spinrcs=os.environ.get('spin_rcs')
rewardrcs=os.environ.get('reward_rcs')

head = CaseInsensitiveDict()
head["rct"] = "1660907496196"
head["screenWidth"] = "393"
head["rcs"] = spinrcs
head["screenHeight"] = "776"
head["reqVersion"] = "2"
head["version"] = "1.1.6"
head["iceToken"] = spinitk
head["Content-Type"] = "application/json"
head["User-Agent"] = "Headline"
head["Accept-Language"] = "en-IN"
head["Content-Length"] = "0"
head["Host"] = "game.buffloft.com"
head["Connection"] = "Keep-Alive"
head["Accept-Encoding"] = "gzip"

headers = CaseInsensitiveDict()
headers["rct"] = "1660908216154"
headers["screenWidth"] = "393"
headers["rcs"] = rewardrcs
headers["screenHeight"] = "776"
headers["reqVersion"] = "2"
headers["version"] = "1.1.6"
headers["iceToken"] = rewardtoken
headers["User-Agent"] = "Headline"
headers["Accept-Language"] = "en-IN"
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Content-Length"] = "127"
headers["Host"] = "game.buffloft.com"
headers["Connection"] = "Keep-Alive"
headers["Accept-Encoding"] = "gzip"

d= ["params=0mZxPXRuX9gUm0K6PgDHXMTrOyQol2faBAXFh3AKlQlUeA6mUaZkXhh1MFNWviqGrm73%2BbvRAWOCM%2BPQOASHkF2MJhTkjW%2BG%2Ba9nzq2%2BzUg%3D",
"params=0mZxPXRuX9gUm0K6PgDHXMTrOyQol2faBAXFh3AKlQlUeA6mUaZkXhh1MFNWviqGTmts%2BHWYJV7JQmhBNhsWp9mA6%2FdSsc65eviTjmhy1dE%3D",
"params=0mZxPXRuX9gUm0K6PgDHXMTrOyQol2faBAXFh3AKlQlUeA6mUaZkXhh1MFNWviqGmpzOb2Sd2qhxkENqomzgrqwGhtuDQItN6wcRiLtpebU%3D"]

for x in d:
  for i in range(10):
    resp = requests.post(url, headers=headers, data=x)
    #message=json.loads(resp.text)
    print(resp.text)
    res = requests.post(url2, headers=head)
    #msg=json.loads(res.text)
    print(res.text)
    time.sleep(2)
    
    

