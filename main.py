import re
import requests

site = requests.get("https://proxyape.com/")
sitetext = site.text
proxy = sitetext
match = re.findall(r'((?:\d{1,3}\.){3}\d{1,3}):(\d+)', proxy)

print(match)
