from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from pytest import raises
from unittest.mock import patch

mock_value = [
    {
        "title": "titulo",
        "reading_time": 1,
    },
    {
        "title": "titulo2",
        "reading_time": 2,
    },
    {
        "title": "titulo3",
        "reading_time": 30,
    },
    {
        "title": "titulo4",
        "reading_time": 10,
    },
]

mock_result = {
    "readable": [
        {
            "unfilled_time": 7,
            "chosen_news": [
                (
                    "titulo",
                    1,
                ),
                (
                    "titulo2",
                    2,
                ),
            ],
        },
        {
            "unfilled_time": 0,
            "chosen_news": [
                (
                    "titulo4",
                    10,
                )
            ],
        },
    ],
    "unreadable": [
        ("titulo3", 30),
    ],
}


def test_reading_plan_group_news():
    with patch(
        "tech_news.analyzer.reading_plan.find_news", return_value=mock_value
    ):
        news = ReadingPlanService.group_news_for_available_time(10)
        assert mock_result == news
    with raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)
