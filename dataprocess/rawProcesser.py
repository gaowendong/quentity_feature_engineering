
import pandas as pd
import numpy as np
import glob

import chardet
# import sys
# sys.path.insert(0, '/Users/kevin_gwdong/djangoproject/tensorflow/lstmPrediction')
from pathlib import Path

import argparse
# initiate the parser
parser = argparse.ArgumentParser()

parser.add_argument("--stockcode", "-sc", help="data stock code")
args = parser.parse_args()

def process_raw():
	path = '/Users/kevin_gwdong/windowsshare/daydata/' 
	
	filename = glob.glob(path + args.stockcode + ".csv")[0]
	# print(filename)
	with open(filename, 'rb') as f:
	    result = chardet.detect(f.read())  # or readline if the file is large

	df = pd.read_csv(filename, encoding=result['encoding'])

	df.drop(df.tail(1).index,inplace=True)

	df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Amount']
	# print(df)
	df = df[df > 0].dropna()
	data_dir = 'data/' + args.stockcode + ".csv"
	df.to_csv(Path(data_dir).resolve(), index=False)

if __name__ == '__main__':
    process_raw()
