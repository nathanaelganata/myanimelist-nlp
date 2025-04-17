import requests
from bs4 import BeautifulSoup
from pwn import log
import pandas as pd
import json
import re

SOURCE = pd.read_csv(r'..\data\raw\top_150_anime_links.csv')
PAGES_TO_SCRAPE = 1

reviews = []

for s in SOURCE['Link']:
    try:
        for p in range(1, PAGES_TO_SCRAPE + 1):
            params = {
                'spoiler': 'on',
                'sort': 'suggested',
                'preliminary': 'on',
                'page': p,
            }

            res = requests.get(s, params=params)
            soup = BeautifulSoup(res.text, 'html.parser')
            
            anime_title = soup.find('h1', class_='title-name').text
            log.info(f'Scraping {anime_title} page {p}...')
            
            reviews_div = soup.find_all('div', class_='review-element')
            for review in reviews_div:
                username = review.find('div', class_='username').text[1:-1]

                update_at_div = review.find('div', class_='update_at')
                date = f'{update_at_div.text} {update_at_div["title"]}'

                recommendation = review.find('div', class_=['tag', 'btn-label', 'js-btn-label']).text

                if review['data-reactions']:
                    reaction_data = json.loads(review['data-reactions'])
                    total_reactions = sum([int(i) for i in reaction_data['count']])
                else:
                    reaction_data = {'count': [0] * 7}

                preliminary_div = review.find('div', class_='preliminary')
                preliminary = True if preliminary_div else False
                episodes_watched = None
                if preliminary:
                    episodes_watched = re.findall(r'[\d/]+', preliminary_div.text.strip())[0]

                content = review.find('div', class_='text').text
                content = content.replace('\n                ', '')
                content = content.replace("“", '"')
                content = content.replace("”", '"')
                content = content.replace("’", "'")
                content = content.replace("‘", "'")
                content = content.replace("–", "-")

                rating = review.find('div', class_='rating').span.text

                review_url = review.find('div', class_='open').a['href']

                user_review_count = review.find('div', class_=['more_reviews', 'js-more_reviews']).a.span.text

                reviews.append({
                    'review_id': review_url.split("=")[1],
                    'anime_title': anime_title, 
                    'review_url': review_url,
                    'date': date,
                    'username': username,
                    'user_review_count': user_review_count,
                    'is_preliminary': preliminary,
                    'episodes_watched': episodes_watched,
                    'recommendation': recommendation,
                    'rating': rating,
                    'review': content,
                    'total_reactions': total_reactions,
                    'nice_count': reaction_data['count'][0],
                    'love_it_count': reaction_data['count'][1],
                    'funny_count': reaction_data['count'][2],
                    'confusing_count': reaction_data['count'][3],
                    'informative_count': reaction_data['count'][4],
                    'well_written_count': reaction_data['count'][5],
                    'creative_count': reaction_data['count'][6],
                })
    except Exception as e:
        log.failure(f'Error parsing {s} page {p}: {e}')

df = pd.DataFrame(reviews)
df.to_csv(r'..\data\raw\top_150_fantasy_reviews.csv', index=False)