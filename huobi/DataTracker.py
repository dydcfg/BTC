__author__ = 'dydcfg'

import thread
import time
import Util
from Util import *
import requests

class DataTracker:
    def setParams(self, interval):
        resp = requests.get(HUOBI_TICKER_BTC)
        resp = resp.json()
        print resp