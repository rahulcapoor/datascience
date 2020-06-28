import json
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import date
import pyodbc
import array as arr
import constants

def readJsonFromFile(file_path):  
    try:
        print ('reading file ', './files/'+file_path)
        with open('./files/'+ file_path) as f:     
            json_from_file = json.load(f)
            if json_from_file:
                connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            "Server=WKWIN9148129;"
                            "Database=Trade;"
                            "Trusted_Connection=yes;") 
                for x in json_from_file["records"]["data"]:
                    if 'CE' in x.keys():                   
                        saveValuesToDb(connection, x["CE"], 'CE')
                    if 'PE' in x.keys():
                        saveValuesToDb(connection, x["PE"], 'PE')
                connection.close()          
    except mysql.connector.Error as error:
        print ("error while reading file {} - {}", file_path, error)
    #finally:       
    #    connection.close()    
  
        
def saveValuesToDb(connection, optionStrike, optionType):
    try:       
        if optionStrike['openInterest'] > 0 :
            SQLCommand = ("INSERT INTO [dbo].[OptionChain]           ([underlying]           ,[strikePrice]           ,[expiryDate]           ,[DownloadDate]           ,[OptionType]           ,[identifier]           ,[openInterest]           ,[changeinOpenInterest]           ,[pchangeinOpenInterest]           ,[totalTradedVolume]           ,[impliedVolatility]           ,[lastPrice]           ,[change]           ,[pChange]           ,[totalBuyQuantity]           ,[totalSellQuantity]           ,[bidQty]           ,[bidprice]           ,[askQty]           ,[askPrice]           ,[underlyingValue])     VALUES           ('{}',{},'{}','{}','{}',  '{}',{},{},{},{}, {},{},{},{},{}, {},{},{},{},{},{})")           
                
            query = SQLCommand.format(optionStrike['underlying'],optionStrike['strikePrice'],optionStrike['expiryDate'], date.today(),
                    optionType, optionStrike['identifier'], optionStrike['openInterest'],
                    optionStrike['changeinOpenInterest'], optionStrike['pchangeinOpenInterest'], optionStrike['totalTradedVolume'],
                    optionStrike['impliedVolatility'], optionStrike['lastPrice'], 
                    optionStrike['change'], optionStrike['pChange'], optionStrike['totalBuyQuantity'],
                    optionStrike['totalSellQuantity'], optionStrike['bidQty'], optionStrike['bidprice'], optionStrike['askQty'], optionStrike['askPrice'],
                    optionStrike['underlyingValue'])
        
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()       
            cursor.close()

    except mysql.connector.Error as error:
        print ("error while saving file into database {} - {}", optionStrike, error)
     
   
def readFromTable():
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=WKWIN9148129;"
                      "Database=Trade;"
                      "Trusted_Connection=yes;")


    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM OptionChain')
    for row in cursor:
        print('row = %r' % (row,))
    
if __name__ == '__main__':
    #for stock in constants.NIFTY_FNO_FILE_NAMES.keys():
    #    readJsonFromFile(constants.NIFTY_FNO_FILE_NAMES[stock])          
    readJsonFromFile('nifty50.json')
    readJsonFromFile('banknifty.json')
   