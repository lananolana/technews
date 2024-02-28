import requests
import rfeed
from bs4 import BeautifulSoup as bs

techcrunch = 'https://techcrunch.com/category/startups/'
r = requests.get('techcrunch')
html = r.text

parser = bs(html,'html.parser')
feed = html.find_all(class_='post-block')
for article in feed:
    link = techcrunch + article.find(class_='post-block__title__link')['href']
    title = article.find(class_='post-block__title').string
    author = article.find(class_='river-byline__authors').string
    description = article.find(class_='post-block__content').string
    image = article.find(class_='post-block__media').find('img')['src']

items_ = []
item = rfeed.Item(title=title,
                  link=link,
                  description = description,
                  author = author,
                  guid = rfeed.Guid(link),
                  enclosure=rfeed.Enclosure(url=image,type='image/jpeg',length=0))
items_.append(item)

feed = rfeed.Feed(title='TechCrunch News',
                  description = 'Startups',
                  language='en-US',
                  items=items_,
                  link=techcrunch)

rss = feed.rss()
