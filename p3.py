from bs4 import BeautifulSoup

import requests

import random



popular_choice = ['motivational', 'life', 'positive', 'friendship', 'success', 'happiness', 'love']





def get_quotes():

    url = "http://www.brainyquote.com/quote_of_the_day.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []

    for quote in soup.find_all('a', {'title': 'view quote'}):

        quotes.append(quote.contents[0])

    random.shuffle(quotes)

    result = quotes

    return result

print(get_quotes())




