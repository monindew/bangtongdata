import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.imdb.com/chart/top/", headers={"User-Agent": "Chrome"})

soup = BeautifulSoup(response.content, "html.parser")

movie_info_list = soup.find('ul', class_='ipc-metadata-list')
# print(movie_info_list.prettify())

# movie_title_list = movie_info_list.find_all('h3')
# print(movie_title_list[0].text)

# movie_rating_list = movie_info_list.find_all("span", class_='ipc-rating-star')
# print(movie_rating_list[0].text)

movie_infos = movie_info_list.find_all("div", class_="cli-children")
# print(movie_infos[0].prettify())

import pandas as pd

df = pd.DataFrame(columns=["rank", "title", "rating"])

i = 0

for info in movie_infos:
    rank_title = info.find('h3', class_='ipc-title__text')
    rank = rank_title.text.split(". ")[0]
    rank = int(rank)
    title = rank_title.text.split(". ")[1]
    rating = info.find(class_='ipc-rating-star').text

    df.loc[i] = [rank, title, rating]
    i += 1

print(df)