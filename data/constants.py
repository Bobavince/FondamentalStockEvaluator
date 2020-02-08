#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setup import sources

from sample.utils.utils import JSON_parsable_Dict

class brokers(JSON_parsable_Dict):
    SAMPLE_BROKER = "broker"

class currencies(JSON_parsable_Dict):
    SAMPLE_currency = "euro"

class capitalisation(JSON_parsable_Dict):
    SAMPLE_capitalisation = "big"

class sources(JSON_parsable_Dict):
    SAMPLE_source = sources.SAMPLE_source

class reference_index(JSON_parsable_Dict):
    SAMPLE_reference_index = "reference_index"