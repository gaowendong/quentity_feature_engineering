
import pandas as pd
import numpy as np
import glob

import chardet
# import sys
# sys.path.insert(0, '/Users/kevin_gwdong/djangoproject/tensorflow/lstmPrediction')
from pathlib import Path

import argparse
# initiate the parser
# parser = argparse.ArgumentParser()

# parser.add_argument("--stockcode", "-sc", help="data stock code")
# args = parser.parse_args()

def process_index(stockcode):
    print(stockcode)
    path = '/Users/kevin_gwdong/windowsshare/indexsdata/' 

    filename = glob.glob(path + str(stockcode) + ".csv")[0]
#     print(filename)
    # print(filename)
    with open(filename, 'rb') as f:
        result = chardet.detect(f.read())  # or readline if the file is large

    df = pd.read_csv(filename, encoding=result['encoding'])

    df.drop(df.tail(1).index,inplace=True)

    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Amount']
    # print(df)
    data_dir = 'data/indexs/' + str(stockcode) + ".csv"
    df.to_csv(Path(data_dir).resolve(), index=False)
    print("finish ", stockcode)

if __name__ == '__main__':
	filename = "../data/Aindexs.csv"
	stocks = pd.read_csv(filename, index_col=False)
	# print(stocks['code'].values)
	for stockcode in stocks['code'].values :
	    process_index(stockcode)
	#     print("finish", stockcode)
