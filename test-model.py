import numpy as np
from keras.models import load_model
from keras.datasets import mnist
import matplotlib.pyplot
import os
import random
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

model = load_model('digit_classification.h5')

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_test = x_test / 255

index = random.randint(0, len(x_test))
img = x_test[index]

img_reshaped = np.reshape(img, [1, 28, 28])

input_prediction = model.predict(img_reshaped)

input_pred_label = np.argmax(input_prediction)

print('Image at index:', index, "\nPredicted:", input_pred_label, "\nActual:", y_test[index])

matplotlib.pyplot.imshow(img)
matplotlib.pyplot.show()

# print(x_test.shape)
# loss, accuracy = model.evaluate(x_test, y_test)
