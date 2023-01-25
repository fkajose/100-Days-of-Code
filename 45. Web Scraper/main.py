import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
titles = soup.find_all(name="h3", class_="title")
titles.reverse()
with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in titles:
        file.write(f"{movie.getText()}\n")
