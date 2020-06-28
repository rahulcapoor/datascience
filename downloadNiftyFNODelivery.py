import requests,csv,json
import constants
from datetime import date
import pandas as pd
import pyodbc
import csv

def downloadNifty50DeliveryInfo(date):
    print ('downloading file for the date %s', date)
    deliveryUrl = "https://archives.nseindia.com/products/content/sec_bhavdata_full_" + date + ".csv"

    fileName = './files/nifty50_delivery.csv'
    
    r = requests.get(deliveryUrl)
    
    with open(fileName,'wb') as f:
        f.write(r.content)  
        
    return fileName

def saveNiftyFNOStocksToDb(deliveryfile):  
    delivery = pd.read_csv(deliveryfile, usecols=['SYMBOL',' SERIES',' DATE1',' PREV_CLOSE',' OPEN_PRICE',' HIGH_PRICE',' LOW_PRICE',' LAST_PRICE',' CLOSE_PRICE',' AVG_PRICE',' TTL_TRD_QNTY',' TURNOVER_LACS',' NO_OF_TRADES',' DELIV_QTY',' DELIV_PER',
])
    df = pd.DataFrame(delivery)
    df.set_index(' SERIES', inplace=True)
    newDf = df.loc[' EQ', :]
    
    newDf.set_index('SYMBOL', inplace=True)
    intDf = newDf.loc[constants.NIFTY_FNO_STOCKS, :]    
    fnoStocks = intDf.dropna()   
    fnoStocks.replace(['-', ' -', ' - '], ['','',''], inplace = True)
  
    connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=WKWIN9148129;"
                        "Database=Trade;"
                        "Trusted_Connection=yes;") 
     
    cursor = connection.cursor()
    
    for i, row in fnoStocks.iterrows():        
        if str(row[' DATE1']) == '' or not row[' DATE1']:
            continue
        cursor.execute('''
                INSERT INTO NiftyDelivery  ([Symbol]           ,[TradeDate]           ,[PreviousClose]           ,[OpenPrice]           ,[HighPrice]           ,[LowPrice]           ,[LastPrice]           ,[ClosePrice]           ,[AvgPrice]           ,[TotalTradedVolume]           ,[NoOfTrades]           ,[DeliveryQuantity]           ,[DeliveryPercentage])
     VALUES           (?           ,?           ,?           ,?           ,?           ,?           ,?           ,?           ,?           ,?           ,?           ,?           ,?)
                ''',
                i,                
                row[' DATE1'],row[' PREV_CLOSE'],row[' OPEN_PRICE'],row[' HIGH_PRICE'],row[' LOW_PRICE']
                ,row[' LAST_PRICE'],row[' CLOSE_PRICE'],row[' AVG_PRICE'],row[' TTL_TRD_QNTY']
                ,row[' NO_OF_TRADES'],row[' DELIV_QTY'],row[' DELIV_PER']
                )
    connection.commit()
    cursor.close()
    connection.close()   
     
    
def run():
    dateRange = pd.bdate_range(start='1/1/2020', end='02/23/2020',  freq='C', weekmask = "Mon Tue Wed Thu Fri", holidays=constants.NIFTY_HOLIDAY_CALENDAR)
    for tradeDate in dateRange:
        print tradeDate
        deliveryFile = downloadNifty50DeliveryInfo(tradeDate.strftime("%d%m%Y"));
        saveNiftyFNOStocksToDb(deliveryFile);
    #saveNiftyFNOStocksToDb('./files/nifty50_delivery.csv'); 

if __name__ == '__main__':
    run()