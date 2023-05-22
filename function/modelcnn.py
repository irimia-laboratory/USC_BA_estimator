
import numpy as np
from pandas import read_csv
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import classification_report
import sklearn
import skimage as ski
import skimage.feature

def get_model(width=128, height=128, depth=64): #3.66
    """Build a 3D convolutional neural network model."""
 
    inputs = tf.keras.Input((width, height, depth, 1))
 
    x = tf.keras.layers.Conv3D(filters=64, kernel_size=3, activation="relu")(inputs)
    x = tf.keras.layers.MaxPool3D(pool_size=2)(x)
    x = tf.keras.layers.BatchNormalization()(x)
 
    x = tf.keras.layers.Conv3D(filters=128, kernel_size=3, activation="relu")(x)
    x = tf.keras.layers.MaxPool3D(pool_size=2)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dropout(0.2)(x)
 
    x = tf.keras.layers.Conv3D(filters=128, kernel_size=3, activation="relu")(x)
    x = tf.keras.layers.MaxPool3D(pool_size=2)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dropout(0.2)(x)
 
    x = tf.keras.layers.GlobalAveragePooling3D()(x)
    x = tf.keras.layers.Dense(units=128, activation="relu")(x)
    x = tf.keras.layers.Dropout(0.3)(x)
 
    outputs = tf.keras.layers.Dense(units=1, activation="relu")(x)
 
    # Define the model.
    model = keras.Model(inputs, outputs, name="3dcnn")
    return model
 
# if __name__ == '__main__':
#     tmp = time.ctime().split(" ")
#     data = filename(tmp)
    #return 0