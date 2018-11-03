from parse_top_trumps_deck import parse_top_trumps_deck
from model.TopTrumpCard import TopTrumpCard
from rank_by_all_statistics import rank_all_top_trumps_cards


x = parse_top_trumps_deck("res/top_trumps_decks/beano_top_trumps_statistics.csv")
y = rank_all_top_trumps_cards(x)
print(y)
