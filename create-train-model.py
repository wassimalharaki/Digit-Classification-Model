import tensorflow as tf
from tensorflow import keras
from keras.datasets import mnist
import keras.layers as layer
import matplotlib.pyplot as plt
import os
tf.random.set_seed(3)
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255

model = keras.Sequential()
model.add(layer.Flatten(input_shape=(28, 28)))      # turns nd into 1d
model.add(layer.Dense(50, activation='relu'))       # y = relu(summation + bias), output/units = 50
model.add(layer.Dense(50, activation='relu'))       # y = relu(summation + bias), output/units = 50
model.add(layer.Dense(10, activation='sigmoid'))    # y = sig(summation + bias), output/units = 10 (10 classes)

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print(model.summary())

history = model.fit(x_train, y_train, epochs=20)

plt.plot(history.history['accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.show()
plt.plot(history.history['loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.show()

model.save("digit_classification.h5")
