import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=171539'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

ogtitle = soup.select_one('meta[property="og:title"]')['content']
ogimage = soup.select_one('meta[property="og:image"]')['content']
ogdescription = soup.select_one('meta[property="og:description"]')['content']

print(ogtitle,ogimage,ogdescription)