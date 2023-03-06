import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(
            url=url, headers={"user-agent": "Fake user-agent"}, timeout=2
        )
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    links = selector.css(".cs-overlay-link::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page = selector.css(".next.page-numbers::attr(href)").get()
    return next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = (
        selector.css("div.pk-share-buttons-wrap")
        .xpath("@data-share-url")
        .get()
    )
    writer = selector.css("a.url.fn.n::text").get()
    title = (
        selector.css("h1.entry-title::text").get().replace("\xa0", " ").strip()
    )
    category = selector.css("span.label::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    reading_time = int(
        selector.css("li.meta-reading-time::text").get().split(" ")[0]
    )
    summary = selector.css(
        ".entry-content > p:nth-of-type(1) *::text"
    ).getall()
    summary = "".join(summary).strip()

    return dict(
        url=url,
        writer=writer,
        title=title,
        category=category,
        reading_time=reading_time,
        timestamp=timestamp,
        summary=summary,
    )


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    result = []

    page = fetch("https://blog.betrybe.com")
    links = scrape_updates(page)

    while len(links) < amount:
        link_next_page = scrape_next_page_link(page)
        page = fetch(link_next_page)
        for link in scrape_updates(page):
            links.append(link)

    for index in range(0, amount):
        page = fetch(links[index])
        scraped_news = scrape_news(page)
        result.append(scraped_news)

    create_news(result)

    return result
