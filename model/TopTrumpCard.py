from typing import List, Callable, Union


class TopTrumpCard:
    __name: str
    __statistic_1: int
    __statistic_2: int
    __statistic_3: int
    __statistic_4: int
    __statistic_5: int
    __statistic_6: int

    def __init__(
        self, name: str,
        statistic_1: int,
        statistic_2: int,
        statistic_3: int,
        statistic_4: int,
        statistic_5: int,
        statistic_6: int
    ):
        self.__name = name
        self.__statistic_1 = statistic_1
        self.__statistic_2 = statistic_2
        self.__statistic_3 = statistic_3
        self.__statistic_4 = statistic_4
        self.__statistic_5 = statistic_5
        self.__statistic_6 = statistic_6

    def name(self):
        return self.__name

    def statistic_1(self):
        return self.__statistic_1

    def statistic_2(self):
        return self.__statistic_2

    def statistic_3(self):
        return self.__statistic_3

    def statistic_4(self):
        return self.__statistic_4

    def statistic_5(self):
        return self.__statistic_5

    def statistic_6(self):
        return self.__statistic_6

    @classmethod
    def all_getters(cls) -> List[Callable[[], Union[str, int]]]:
        return [ cls.name ] + cls.all_statistics()

    @classmethod
    def all_statistics(cls) -> List[Callable[[], int]]:
        return [
            cls.statistic_1,
            cls.statistic_2,
            cls.statistic_3,
            cls.statistic_4,
            cls.statistic_5,
            cls.statistic_6,
        ]
