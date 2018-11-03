from typing import List
from model.TopTrumpCard import TopTrumpCard


def rank_all_top_trumps_cards(cards: List[TopTrumpCard]) -> List[TopTrumpCard]:
    statistics_functions = TopTrumpCard.all_statistics()
    statistics_functions_names = [statistics_function.__name__ for statistics_function in statistics_functions]
    card_keys = [card.name() for card in cards]
    ranked_by_statistics_function_per_statistics_function = {
        statistics_function.__name__: {
            name: index + 1
            for index, name
            in enumerate(card.name() for card in sorted(cards, key=statistics_function, reverse=True))
        }
        for statistics_function
        in statistics_functions
    }
    return [
        TopTrumpCard(
            card_key, **{
                statistics_functions_name:
                    ranked_by_statistics_function_per_statistics_function[statistics_functions_name][card_key]
                for statistics_functions_name
                in statistics_functions_names
            }
        ) for card_key
        in card_keys
    ]
