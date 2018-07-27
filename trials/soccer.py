#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:35:47 2018

@author: matthew.gonzalez
"""

import pandas as pd

submissions = pd.read_csv('soccer_sub.csv')
games = pd.read_csv('Games.csv')
submissions['date'] = pd.to_datetime(submissions['date'])
games['date'] = pd.to_datetime(games['date'])

new = pd.merge(submissions, games, how='left', on='date')