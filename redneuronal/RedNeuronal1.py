import tensorflow
import numpy as np

celsius =np.array([-40,-10,0,8,15,22,38], dtype=float)
fahrenheit =np.array([-40,-14,32,46,59,72,100], dtype=float)

capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer = tf.keras.optimizer.Adam(0.1),
loss='mean_squared_error
)'


