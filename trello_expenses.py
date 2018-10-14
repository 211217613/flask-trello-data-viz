#!/usr/bin/python
from trollop import TrelloConnection

import logging
from math import ceil
from time import strftime
import json
import seaborn as sns
import matplotlib.pyplot as plt


# idBoard': '577b17583e5d17ee55b20e44',
# idList': '577b17583e5d17ee55b20e45',
MONTHS = ['jan', 'feb', 'March', 'April', 'May', 'June', 'July', 'Aug',
          'sept', 'oct', 'Nov', 'Dec']
USDMXN = {
    'jan': 20.8340,
    'dec': 20.7275,
    'nov': 20.5720,
    'oct': 18.8640,
    'sept': 19.3850,
    'aug': 18.7851,
    'july': 18.752
}


class FrozenDict(object):
    def __init__(self, *args, **kwargs):
        # Hack to bypass `__setattr__`.
        self.__dict__['d'] = dict(*args, **kwargs)

    def __getattr__(self, key):
        return self.d[key]

    def __setattr__(self, key, val):
        raise TypeError('FrozenDict does not support setting attributes.')

    def __delattr__(self, key, val):
        raise TypeError('FrozenDict does not support deleting attributes.')


def read_settings():
    with open('keys.json', 'r') as data:
        keys = json.load(data)
        return FrozenDict({
            'token':   keys["token"],
            'api_key': k["api_key"],
            'board': 'BE89pW61'
        })


def get_total_per_month(month, board_list):
    """Sums all the values in a month board.
    :param month: The month to calculate total for
    :param board_list: The entire Trello Board
    :return: The sum for the month not rounded
    """
    month = month.lower()
    total = sum(
        float(crd.name.split('-')[1])
        for lst in board_list if month in lst.name.lower() for crd in lst.cards
    )
    if total > 1000:
        return total / USDMXN[month]
    else:
        return total


def first_of_the_month():
    day = strftime("%d")
    if '1' is day:
        pass


def get_yearly_average(totals):
    sum = 0.0
    count = 0
    for month in totals:
        if month != 0.0:
            count = count + 1
            sum += month
            # print month
    year_average = sum / count
    print 'year ave {}'.format(str(year_average))
    return year_average


def plot(totals, average):
    sns.set(style='white', font_scale=1.5)
    plt.title('Monthly Food Expenses')
    plt.xlabel('Months')
    plt.ylabel('Pesos')
    sns.barplot(x=MONTHS, y=totals)
    plt.show()


def main():
    costs = list()
    names = list()

    # Establish connection
    conn = TrelloConnection(SETTINGS.api_key, SETTINGS.token)
    logging.info("Iterating through boards...")

    board = conn.get_board(SETTINGS.board)
    totals = [get_total_per_month(month, board.lists) for month in MONTHS]
    print totals
    average = get_yearly_average(totals)
    logging.info(totals)
    logging.debug('Board list: {}'.format(board.lists))
    plot(totals, average)


if __name__ == '__main__':
    SETTINGS = read_settings()

    # Set up basic logging
    logging.basicConfig(
        format='%(levelname)s %(message)s',
        level=logging.DEBUG,
        filename='DEBUG.log',
        filemode='w'
    )
    main()
