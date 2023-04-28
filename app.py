from flask import Flask, render_template
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

model = load_model('digit_classification.h5')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", prediction=None)

@app.route("/submit/<imgname>")
def predict(imgname):
    abs_path = "/Users/Admin/Downloads/" + imgname

    image = cv2.imread(abs_path)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    image = cv2.resize(image, (28, 28))

    image = image / 255

    plt.imshow(image)
    plt.show()

    image = np.reshape(image, [1, 28, 28])

    pred = model.predict(image)

    pred = np.argmax(pred)

    return render_template("index.html", prediction=pred)

if __name__ == "__main__":
    app.run()
