import tensorflow as tf
from tensorflow import keras

def get_model(width=128, height=128, depth=128): 
 
    inputs = tf.keras.Input((width, height, depth, 1))
 
    x = tf.keras.layers.Conv3D(filters=16, kernel_size=6, activation="relu")(inputs)
    x = tf.keras.layers.MaxPool3D(pool_size=2)(x)
    x = tf.keras.layers.BatchNormalization()(x)
 
    x = tf.keras.layers.Conv3D(filters=32, kernel_size=6, activation="relu")(x)
    x = tf.keras.layers.MaxPool3D(pool_size=2)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dropout(0.2)(x)
 
    x = tf.keras.layers.Conv3D(filters=64, kernel_size=6, activation="relu")(x)
    x = tf.keras.layers.MaxPool3D(pool_size=2)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dropout(0.2)(x)
      
    x = tf.keras.layers.Conv3D(filters=128, kernel_size=6, activation="relu")(x)
    x = tf.keras.layers.MaxPool3D(pool_size=2)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dropout(0.2)(x)
    
    x = tf.keras.layers.GlobalAveragePooling3D()(x)
    x = tf.keras.layers.Dense(units=128, activation="relu")(x)
    x = tf.keras.layers.Dropout(0.3)(x)
 
    outputs = tf.keras.layers.Dense(units=1, activation="relu")(x)
 
    # Define the model.
    model = keras.Model(inputs, outputs, name="BA_3DCNN_conv4k6d2")
    return model
 
