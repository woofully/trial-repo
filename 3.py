#!/usr/bin/env python

# -*- coding: UTF-8 -*-

import csv
import codecs

with open('shanghai1.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('shanghai1.csv', 'w',encoding='utf-8') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(lines)