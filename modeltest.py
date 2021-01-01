# Neural networks.
import tensorflow.keras as kr

# Numerical arrays
import numpy as np

# Data frames.
import pandas as pd

df = pd.read_csv("powerproduction.csv")

#Remove power of zero where windspeed is above 10
df = df.drop(df[(df.speed > 10) & (df.power == 0)].index)

train = df

model = kr.models.Sequential()
model.add(kr.layers.Dense(50, input_shape=(1,), activation='sigmoid', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
model.add(kr.layers.Dense(1, activation='linear', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
model.compile(kr.optimizers.Adam(lr=0.001), loss='mean_squared_error')

model.fit(train['speed'], train['power'], epochs=500, batch_size=10)

while True:
    n = float(input("number"))
    print(model.predict([n]))