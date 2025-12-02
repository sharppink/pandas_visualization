#!pip install datetime
#!pip install pykrx
#!pip install tensorflow
#!pip install sklearn
#!pip install matplotlib
import sys
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlob.dates as mdates
from sklearn.keras.models import Model
from tensorflow.keras.layers import(
    Input, Dense, Dropout, LayerNormalization, MultiHeadAttention, Add, GlobalAveragePooling1D
)
from tensorflow.keras.optimizers import Adam
from datetime import datetime
from pykrx import stock

#005930
value = sys.argv[1]  

result = stock.get_market_ohlcv_by_date(fromdate="20200101", todate="20241231", ticker=value)

print(result.to_csv(index=True))

def transfromer_decoder():
    