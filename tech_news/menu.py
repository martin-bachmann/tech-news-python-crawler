# Requisitos 11 e 12
import sys
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title,
)

from tech_news.scraper import get_tech_news


def get_tech_news_option():
    value = int(input("Digite quantas notícias serão buscadas:"))
    return get_tech_news(value)


def search_by_title_option():
    value = input("Digite o título:")
    return search_by_title(value)


def search_by_date_option():
    value = input("Digite a data no formato aaaa-mm-dd:")
    return search_by_date(value)


def search_by_category_option():
    value = input("Digite a categoria:")
    return search_by_category(value)


def end():
    print("Encerrando script")
    return


def analyzer_menu():
    """Seu código deve vir aqui"""
    functions = [
        get_tech_news_option,
        search_by_title_option,
        search_by_date_option,
        search_by_category_option,
        top_5_categories,
        end,
    ]
    try:
        option = input(
            """Selecione uma das opções a seguir:\n"""
            """ 0 - Popular o banco com notícias;\n"""
            """ 1 - Buscar notícias por título;\n"""
            """ 2 - Buscar notícias por data;\n"""
            """ 3 - Buscar notícias por categoria;\n"""
            """ 4 - Listar top 5 categorias;\n"""
            """ 5 - Sair.\n"""
        )

        print(functions[int(option)]())
    except (IndexError, TypeError, ValueError):
        print("Opção inválida", file=sys.stderr)
