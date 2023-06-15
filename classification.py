import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.metrics import confusion_matrix
import seaborn as sns
from keras.preprocessing import image
from PIL import Image

train_df = pd.read_csv("/Users/dhruvchowdhary/FashionAI/process_data.csv")

print(train_df.head())

np.random.seed(123)
np.random.shuffle(train_df.values)

x_train = train_df

