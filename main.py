from get_news_data import *
from get_news_urls import *
import asyncio
import aiohttp
 

async def get_all_urls():
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.ensure_future(url_bisnis(session)),          
            asyncio.ensure_future(url_emiten(session)),            
            asyncio.ensure_future(url_invest(session)),            
            asyncio.ensure_future(url_kadata(session)),            
            asyncio.ensure_future(url_kompas(session))
            ]

        return await asyncio.gather(*tasks)

async def get_all_news():
    all_url = await get_all_urls()
    connector = aiohttp.TCPConnector(limit=5)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for urls in all_url:
            for url in urls:
                if "bisnis" in url:
                    tasks.append(asyncio.ensure_future(get_news_bisnis(url, session)))
                if "kompas" in url:
                    tasks.append(asyncio.ensure_future(get_news_kompas(url, session)))
                if "katada" in url:
                    tasks.append(asyncio.ensure_future(get_news_kadata(url, session)))
                if "invest" in url:
                    tasks.append(asyncio.ensure_future(get_news_invest(url, session)))
                if "emiten" in url:
                    tasks.append(asyncio.ensure_future(get_news_emiten(url, session)))

        await asyncio.gather(*tasks)

asyncio.run(get_all_news())







