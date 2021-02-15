import requests
from bs4 import BeautifulSoup
from pprint import pprint

uri = 'https://news.ycombinator.com/news'


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn


def create_multi_custom_hn(page):
    hn = []
    for i in range(1, page + 1):
        if i == 1:
            res = requests.get(uri)
            soup = BeautifulSoup(res.text, 'html.parser')
        else:
            res = requests.get(uri + f'?p={i}')
            soup = BeautifulSoup(res.text, 'html.parser')

        links = soup.select('.storylink')
        subtext = soup.select('.subtext')

        hn.extend(create_custom_hn(links, subtext))
    return sort_stories_by_votes(hn)


pprint(create_multi_custom_hn(3))
