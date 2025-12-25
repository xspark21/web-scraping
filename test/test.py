import requests


link = requests.get("https://github.com/xspark21/web-scraping", timeout = 10).text
