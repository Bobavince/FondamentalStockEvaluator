#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Dict

import requests
import pprint

headers = {
    'Referer': 'https://www.bloomberg.com/quote/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36',
    'DNT': '1',
}


# =========== HISTORICAL DATA ===========
params_sample_1= (
    ('timeframe', '5_YEAR'),
    ('period', 'daily'),
    ('volumePeriod', 'daily'),
)


def get_5_years():
    return ('timeframe', '5_YEAR')

def get_daily():
    return (('period', 'daily'),
    ('volumePeriod', 'daily'))

def get_weekly():
    return (('period', 'weekly'),
    ('volumePeriod', 'weekly'))

# =========== META DATA ===========

params_sample_2 = (
    ('locale', 'en'),
    ('customTickerList', 'true'),
)

params_sample_3 = (
    ('days', '2'),
    ('interval', '10'),
    ('volumeInterval', ''),
)


def request_history(ticket : str, params :tuple) -> Dict:
    response = requests.get(f'https://www.bloomberg.com/markets2/api/history/{ticket.replace(":","%3")}/PX_LAST', headers=headers, params=params)
    pprint.pprint(response.json())

    return response.json()

def request_datastrip(ticket : str, params :tuple) -> Dict:
    response = requests.get(f'https://www.bloomberg.com/markets2/api/datastrip/{ticket.replace(":","%3")}', headers=headers, params=params)
    pprint.pprint(response.json())

    return response.json()


def request_intraday(ticket : str, params :tuple) -> Dict:
    response = requests.get(f'https://www.bloomberg.com/markets2/api/intraday/{ticket.replace(":","%3")}', headers=headers, params=params)
    pprint.pprint(response.json())

    return response.json()



def get_5years_weekly(ticket : str):
    params = get_5_years() + get_weekly()
    request_history(ticket, params)


def get_5years_daily(ticket : str):
    params = get_5_years() + get_daily()
    request_history(ticket, params)

if __name__ == '__main__':
    # get_5years_daily("INDU:AIND")
    # get_5years_weekly("INDU:AIND")
    # request_datastrip("INDU:AIND", params_sample_2)
    # request_intraday("INDU:AIND", params_sample_3)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.bloomberg.com/markets2/api/history/INDU%3AIND/PX_LAST?timeframe=5_YEAR&period=weekly&volumePeriod=weekly', headers=headers)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.bloomberg.com/markets2/api/datastrip/INDU%3AIND%2CSPX%3AIND%2CCCMP%3AIND?locale=en&customTickerList=true', headers=headers)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.bloomberg.com/markets2/api/intraday/KO%3AUS?days=2&interval=10&volumeInterval=', headers=headers)
