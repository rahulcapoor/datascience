import requests
import os, ssl
import nsepy
from requests import Session
from functools import partial
from constants import URLFetch
import constants

session = Session()
headers = {'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, sdch, br',
           'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
           'Connection': 'keep-alive',
           'Host': 'www1.nseindia.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest'}


URLFetchSession = partial(URLFetch, session=session,
                          headers=headers)

option_chain_url = URLFetchSession(url = "http://www.nseindia.com/api/option-chain-%s/?symbol=%s")

def downloadStockOptionChain(derivativeType ,stock_name, file_name):
    print('download data for ', stock_name)  
    response = option_chain_url(derivativeType, stock_name)
    file = open('./files/'+file_name, "w")
    file.write(response.content)
    file.close()

def run():
    for stock in constants.NIFTY_FNO_FILE_NAMES.keys():
        downloadStockOptionChain('equities', stock, constants.NIFTY_FNO_FILE_NAMES[stock])  
    downloadStockOptionChain('indices', 'NIFTY', 'nifty50.json')
    downloadStockOptionChain('indices', 'BANKNIFTY', 'banknifty.json')

    

if __name__ == '__main__':
    run()