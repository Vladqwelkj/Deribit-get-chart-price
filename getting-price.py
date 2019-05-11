###
START_TIME = datetime.datetime(2019, 4, 11,   0,00)
START_TIME = datetime.datetime.now()
INSTRUMENT_NAME = 'BTC-PERPETUAL'
RESOLUTION = 5

FILENAME = 'prices.txt'
###

import requests
import json
import datetime
import time

start_unix = time.mktime(START_TIME.timetuple())*1000
stop_unix = time.mktime(START_TIME.timetuple())*1000

params = {
	'instrument_name': INSTRUMENT_NAME,
	'START_TIMEstamp': int(start_unix),
	'end_timestamp': int(stop_unix),
	'resolution': RESOLUTION
}
result = requests.get('https://deribit.com/api/v2/public/get_tradingview_chart_data', params=params).json()['result']
ohlc = []
for index, Open in enumerate(result['open']):
	ohlc.append([Open, result['high'][index], result['low'][index], result['close'][index]])

open(FILENAME, 'w')
f = open(FILENAME, 'a')
for val in ohlc:
	val[0] = int(val[0]) if int(val[0])==val[0] else val[0]
	val[1] = int(val[1]) if int(val[1])==val[1] else val[1]
	val[2] = int(val[2]) if int(val[2])==val[2] else val[2]
	val[3] = int(val[3]) if int(val[3])==val[3] else val[3]
	f.write(str(val[0])+' '+str(val[1])+' '+str(val[2])+' '+str(val[3])+'\n')

print('length:', len(ohlc))