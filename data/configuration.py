#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from data import constants
from sample.utils.utils import JSON_parsable_Dict

class configuration(JSON_parsable_Dict):
    reference_money = "euro"
    default_stock_source = constants.sources.SAMPLE_source
    default_broker = constants.brokers.SAMPLE_BROKER