__author__ = 'dydcfg'

import thread
import time
import Util
from Util import *
import requests
import datetime
import json

class DataTracker:
    def track(self, interval):
        flag = ""
        while True:
            myTime = datetime.datetime.now()
            resp = requests.get(HUOBI_TICKER_BTC)
            resp = resp.json()
            print resp["trades"][0]
            if flag != resp["trades"][0]:
                filename = str(myTime.year)+str(myTime.month)+str(myTime.day)+".data"
                print filename
                fp = open(filename,'a+')
                fp.write(json.dumps(resp)+"\n")
                fp.close()
                flag = resp["trades"][0]
            time.sleep(interval)

