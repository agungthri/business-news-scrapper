import bs4


async def url_emiten(session):
    main_url_emiten = "https://www.emitennews.com/search/"
    async with session.get(main_url_emiten) as data:
        data = await data.text()
        soup = bs4.BeautifulSoup(data, 'html.parser')
        in_link = "https://www.emitennews.com/news/"
        all_url = []
        for link in soup.find_all("a"):
            url = link.get('href')
            if (url != None) and (in_link in url):
                all_url.append(url)
        return set(all_url)


async def url_bisnis(session):
    main_url_bisnis = "https://www.bisnis.com/index"
    async with session.get(main_url_bisnis) as data:
        data = await data.text()
        soup = bs4.BeautifulSoup(data, "html.parser")
        in_link = "bisnis.com/read/"
        all_url = []
        for link in soup.find_all("a"):
            url = link.get("href")
            if (url != None) and (in_link in url):
                all_url.append(url)
        return set(all_url)


async def url_kompas(session):
    main_url_kompas = "https://money.kompas.com/search"
    async with session.get(main_url_kompas) as data:
        data = await data.text()
        soup = bs4.BeautifulSoup(data, "html.parser")
        in_link = "https://money.kompas.com/read"
        all_url = []
        for link in soup.find_all("a"):
            url = link.get("href")
            if (url != None) and (in_link in url):
                all_url.append(url)
        return set(all_url)


async def url_invest(session):
    main_url_invest = "https://investor.id/indeks"
    async with session.get(main_url_invest) as data:
        data = await data.text()
        soup = bs4.BeautifulSoup(data, "html.parser")
        in_link = "https://investor.id/"
        all_url = []
        for link in soup.find_all("a"):
            url = link.get("href")
            if (url != None) and (in_link in url):
                if len(url.split("-")) > 3:
                    all_url.append(url)
        return set(all_url)


async def url_kadata(session):
    main_url_kadata = "https://katadata.co.id/indeks/listing"
    async with session.get(main_url_kadata) as data:
        data = await data.text()
        soup = bs4.BeautifulSoup(data, "html.parser")
        in_link = "https://katadata.co.id/"
        all_url = []
        for link in soup.find_all("a"):
            url = link.get("href")
            if (url != None) and (in_link in url):
                if len(url.split("/")) > 5:
                    all_url.append(url)
        return set(all_url)
