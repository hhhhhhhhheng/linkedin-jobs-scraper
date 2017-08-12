# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:40:28 2017

@author: hengh
"""
import pandas

def convert():
    pandas.read_json('input.txt').to_excel('output.xlsx')
    return 0

convert()
