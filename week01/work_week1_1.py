
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent': user_agent}

url = 'https://maoyan.com/films?showType=3'

response = requests.get(url, headers=header)

bs_info = bs(response.text, 'html.parser')

movie_details = []
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    name = tags.find('span', attrs={'class': 'name'}).text
    scores = tags.find('span', attrs={'class': 'score channel-detail-orange'})
    if scores is not None:
        integer = scores.find('i', attrs={'class': 'integer'}).text
        fraction = scores.find('i', attrs={'class': 'fraction'}).text
        movie_score = integer+fraction
    else:
        movie_score = 'no score'
    for divs in tags.find_all('div', attrs={'class': 'movie-hover-title'}):
        for spans in divs.find_all('span', attrs={'class': 'hover-tag'}):
            if spans.text == '类型:':
                spans.replace_with('')
                movie_type = divs.text.replace(' ', '').strip()
    movie_detail = [name, movie_score, movie_type]
    movie_details.append(movie_detail)

movie = pd.DataFrame(data=movie_details[:10])
movie.to_csv('./movie.csv', encoding='utf-8', index=False, header=['影片名称', '评分', '种类'])