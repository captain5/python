#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import re
import datetime
import os

filename = 'output_1981.10.21.txt'
get_date = re.search('(?P<Year>\d{4})\.(?P<Month>\d{2})\.(?P<Day>\d{2})', filename)
year = get_date.group('Year')
month = get_date.group('Month')
day = get_date.group('Day')
weekday = datetime.datetime(int(year), int(month), int(day)).strftime('%w')
new_filename = 'output_' + year + '-' + month + '-' + day + '-' + weekday + '.txt'
if os.path.exists(filename) == False:
	os.system('touch output_1981.10.21.txt')
os.rename(filename, new_filename)
