import bs4
from nlp import *


async def get_news_bisnis(url_bisnis, session):
    async with session.get(url_bisnis) as data:
        data = await data.text()
        data = bs4.BeautifulSoup(data, 'html.parser')
        data = data.find_all("p")
        text = ". ".join([i.text for i in data])
        to_summarize(text, url_bisnis)


async def get_news_kompas(url_kompas, session):
    async with session.get(url_kompas) as data:
        data = await data.text()
        data = bs4.BeautifulSoup(data, 'html.parser')
        data = data.find_all("p")
        text = ". ".join([i.text for i in data])
        to_summarize(text, url_kompas)


async def get_news_emiten(url_emiten, session):
    async with session.get(url_emiten) as data:
        data = await data.text()
        data = bs4.BeautifulSoup(data, 'html.parser')
        data = data.find_all(attrs={"class":"text-detail-news dual-theme"})
        text = ". ".join([i.text for i in data])
        to_summarize(text, url_emiten)


async def get_news_invest(url_invest, session):
    async with session.get(url_invest) as data:
        data = await data.text('latin-1')
        data = bs4.BeautifulSoup(data, 'html.parser')
        data = data.find_all("p")
        text = ". ".join([i.text for i in data])
        to_summarize(text, url_invest)


async def get_news_kadata(url_kadata, session):
    async with session.get(url_kadata) as data:
        data = await data.text()
        data = bs4.BeautifulSoup(data, 'html.parser')
        data = data.find_all("p")
        text = ". ".join([i.text for i in data])
        to_summarize(text, url_kadata)

