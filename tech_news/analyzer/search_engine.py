# Requisito 7
from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):
    """Seu código deve vir aqui"""
    result = []
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    for item in data:
        result.append((item["title"], item["url"]))
    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    result = []
    try:
        data = search_news(
            {
                "timestamp": datetime.strptime(date, "%Y-%m-%d").strftime(
                    "%d/%m/%Y"
                )
            }
        )
        for item in data:
            result.append((item["title"], item["url"]))
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    result = []
    data = search_news({"category": {"$regex": category, "$options": "i"}})
    for item in data:
        result.append((item["title"], item["url"]))
    return result
