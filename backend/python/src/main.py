import os
import chess
import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers


normalized_csv = 'chess_normalized.csv'

def access_data(data_dir):
    os.chdir(data_dir)
    df = pd.read_csv(normalized_csv)
    data = df['moves'].tolist()[:500]
    split_data = []
    indice = 500


