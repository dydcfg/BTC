#coding=utf-8
import hashlib
import time
import urllib
import requests





#在此输入您的Key
ACCESS_KEY = "aca54373-0ee9bc91-ee676ae2-af63c"
SECRET_KEY = "6bbe048a-90808654-73547109-8a744"

HUOBI_TICKER_BTC="http://api.huobi.com/staticmarket/detail_btc_json.js"
HUOBI_SERVICE_API="https://api.huobi.com/apiv3"
ACCOUNT_INFO = "get_account_info"
GET_ORDERS = "get_orders"
ORDER_INFO = "order_info"
BUY = "buy"
BUY_MARKET = "buy_market"
CANCEL_ORDER = "cancel_order"
NEW_DEAL_ORDERS = "get_new_deal_orders"
ORDER_ID_BY_TRADE_ID = "get_order_id_by_trade_id"
SELL = "sell"
SELL_MARKET = "sell_market"

'''
发送信息到api
'''
def send2api(pParams, extra):
	pParams['access_key'] = ACCESS_KEY
	pParams['created'] = int(time.time())
	pParams['sign'] = createSign(pParams)
	if(extra) :
		for k in extra:
			v = extra.get(k)
			if(v != None):
				pParams[k] = v
		#pParams.update(extra)
	tResult = httpRequest(HUOBI_SERVICE_API, pParams)
	return tResult

'''
生成签名
'''
def createSign(params):
	params['secret_key'] = SECRET_KEY;
	params = sorted(params.items(), key=lambda d:d[0], reverse=False)
	message = urllib.urlencode(params)
	#message = urllib.parse.urlencode(params)
	message=message.encode(encoding='UTF8')
	m = hashlib.md5()
	m.update(message)
	m.digest()
	sig=m.hexdigest()
	return sig

'''
request
'''
def httpRequest(url, params):
    postdata = urllib.urlencode(params)
    postdata = postdata.encode('utf-8')
    fp = requests.post(url, params = postdata)

    if fp.status_code != 200:
        return None

    else:
		#mybytes = fp.read()
		#mystr = mybytes.decode("utf8")
		#fp.close()
		mystr = fp.json()
		return mystr



