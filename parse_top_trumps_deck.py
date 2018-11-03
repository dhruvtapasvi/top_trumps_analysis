import csv
from model.TopTrumpCard import TopTrumpCard
from typing import List


def parse_top_trumps_deck(file_name: str) -> List[TopTrumpCard]:
    arg_names = [ getter.__name__ for getter in TopTrumpCard.all_getters()]
    with open(file_name, "r") as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)
        return [
            TopTrumpCard(**{arg_name: column for arg_name, column in zip(arg_names, row)})
            for row
            in csv_reader
        ]
