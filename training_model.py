import cv2
import os
import numpy as np
import pickle
import re
from imutils import paths
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Flatten, Dense
from helpers import resize_to_fit

data = []
labels = []
file_img_base = "./projeto_find/separate_captcha_database"

imgs = paths.list_images(file_img_base)

for file in imgs:
    label = file.split(os.path.sep)[-2]
    image = cv2.imread(file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #padronize image 20x20px]
    image = resize_to_fit(image, 20, 20)
    #add dimention for keras read image
    image = np.expand_dims(image, axis=2)
    #add elements to lists
    labels.append(label)
    data.append(image)

data = np.array(data, dtype="float") / 255
labels = np.array(labels)

#separe on train data(75%) and test data(25%)
(X_train, X_test, Y_train, Y_test) = train_test_split(data, labels, test_size=0.25, random_state=0)

#convert with one-hot encoding
lb = LabelBinarizer().fit(Y_train)
Y_train = lb.transform(Y_train)
Y_test = lb.transform(Y_test)

#salve labelBinarizer in a file with peckle
label_model_path = "./projeto_find/model_labels.dat"
with open(label_model_path, "wb") as pickle_file:
    pickle.dump(lb, pickle_file)

#create and training AI
model = Sequential()

#creating neural network layers
#first layer
model.add(Conv2D(20, (5,5), padding="same", input_shape=(20, 20, 1), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

#second layer
model.add(Conv2D(50, (5,5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

#third layer
model.add(Flatten())
model.add(Dense(500, activation="relu"))

#scape layer
model.add(Dense(10, activation="softmax"))

#to compile all layers
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

#training AI
model.fit(X_train, Y_train, validation_data=(X_test, Y_test), batch_size=10, epochs=20, verbose=1)

#save model in a file
model.save("./projeto_find/trained_model.keras")

