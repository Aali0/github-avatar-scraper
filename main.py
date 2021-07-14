import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github Username: ')
url = 'http://github.com/' + github_user
req = requests.get(url)
soup = bs(req.content, 'html.parser')
profile_pic = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_pic)
