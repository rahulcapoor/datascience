import sys
import getopt
from fetchFrame import fetch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def main(argv):
    inputfile = ''
    stockName = ''

    try:
        opts, args = getopt.getopt(argv, "hf:s:", ["ffile=", "sname="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'PlotFnODeliveryStocks.py -f <filePath> -s <stockName>'
            sys.exit()
        elif opt in ("-f", "--ffile"):
            inputfile = arg
        elif opt in ("-s", "--sname"):
            stockName = arg
    
    query = "select * from [dbo].[NiftyDelivery] where Symbol = '{}'".format(stockName) 
    df = fetch(query)
    df = df.set_index(pd.DatetimeIndex(df['TradeDate'].values))
    
    plt.figure(figsize=(12.2, 4.5))
    plt.plot(df['DeliveryQuantity'], label='Del Quan.')
    plt.title('Delivery Quantity History')
    plt.xlabel('Date')
    plt.ylabel('Delivery Quantity')
    plt.show()
    
    N = len(df)
    ind = np.arange(N)
    width = 0.35
    
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    
    tradedQuantity = df.loc[: , "TotalTradedVolume"]
    deliveryQuantity = df.loc[: , "DeliveryQuantity"]
    
    ax.bar(ind+ 0.00, tradedQuantity, width, color='r')
    ax.bar(ind+ 0.3, deliveryQuantity, width, color='b')
    
    ax.set_ylabel('quanity')
    #ax.set_xticks(ind, df.loc[: , "TradeDate"])    
    
    ax.set_yticks(np.arange(0,10000000, 10000))
    ax.legend(labels=['Total Trades', 'Delivery'])
    plt.show()    

if __name__ == '__main__':
    main(sys.argv[1:])
