#Import Modules
# Neural networks.
import tensorflow.keras as kr

# Numerical arrays
import numpy as np

# Data frames.
import pandas as pd

# Read in data file into pandas dataframe
df = pd.read_csv("powerproduction.csv")

#Remove power of zero where windspeed is above 10 (non-sensical data points)
df = df.drop(df[(df.speed > 10) & (df.power == 0)].index)

# Create training set - in this case, use whole dataset
train = df

# Create model
model = kr.models.Sequential()

# Add first layer
model.add(kr.layers.Dense(50, input_shape=(1,), activation='sigmoid', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))

# Add output layer
model.add(kr.layers.Dense(1, activation='linear', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))

# Compile model
model.compile(kr.optimizers.Adam(lr=0.001), loss='mean_squared_error')

# Fit model to training sety
model.fit(train['speed'], train['power'], epochs=500, batch_size=10)

# Save model in format to allow use of model in tensorflow.js
model.save("model.h5")

#print(model.predict([15]))