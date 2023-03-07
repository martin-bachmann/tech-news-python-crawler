# Requisito 10
from collections import Counter
from tech_news.database import find_news


def top_5_categories():
    """Seu código deve vir aqui"""
    result = []
    news = find_news()
    categories = Counter([item["category"] for item in news])
    for category in sorted(
        categories.items(), key=lambda item: (-item[1], item[0])
    ):
        result.append(category[0])
    return result
