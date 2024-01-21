import requests
from bs4 import BeautifulSoup

# A function to get the rankings of top 30 universities from www.shanghairanking.com/arwu/2023
def fetch_university_rankings(url, rank_index, name_index, score_index):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for row in soup.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) > max(rank_index, name_index, score_index):
            rank = columns[rank_index].text.strip()
            name = columns[name_index].text.strip()
            score = columns[score_index].text.strip()
            print(f"{rank}: {name} - Score: {score}")


ranking_url = 'https://www.shanghairanking.com/rankings/arwu/2023'

# Indices for the parsing logic. Indicates the position of an element from left to right in a list.
rank_index = 0  # Index of the td tag for rank
name_index = 1  # Index of the td tag for university name
score_index = 4  # Index of the td tag for score

fetch_university_rankings(ranking_url, rank_index, name_index, score_index)
