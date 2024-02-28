from keras import backend as K
from keras import layers
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Activation
from keras.layers import Flatten
from keras.layers import Dense
from keras.datasets import mnist
from keras import utils
from keras.optimizers import SGD, RMSprop, Adam
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator


class LeNetwork:
  @staticmethod
  def build(input_shape, classes):
    model = Sequential()

    resize_and_rescale = Sequential([
      layers.Resizing(28, 28),
      layers.Rescaling(1./255)
    ])

    data_augmentation = Sequential([
      layers.RandomFlip("horizontal_and_vertical"),
      layers.RandomRotation(0.2)
    ])

    model.add(resize_and_rescale)
    model.add(data_augmentation)

    model.add(Conv2D(20, kernel_size=5, padding="same",
    input_shape=input_shape))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(50, kernel_size=5, padding="same"))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

    # Flatten => RELU layers
    model.add(Flatten())
    model.add(Dense(500))
    model.add(Activation("relu"))
    # building a softmax classifier
    model.add(Dense(classes))
    model.add(Activation("softmax"))

    return model

# network construction and training process
NB_EPOCH = 40
BATCH_SIZE = 128
VERBOSE = 1
OPTIMIZER = Adam()
VALIDATION_SPLIT=0.2
IMG_ROWS, IMG_COLS = 28, 28 # these are the input image dimensions
NB_CLASSES = 10 # number of class labels or outputs
#INPUT_SHAPE = (1, IMG_ROWS, IMG_COLS)
INPUT_SHAPE = (IMG_ROWS, IMG_COLS, 1)
# split data between train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()
K#.common.set_image_dim_ordering("tf")
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# please note that we need a 60K x [1 x 28 x 28] shape as input to the CNN
#X_train = X_train[:, np.newaxis, :, :]
#X_test = X_test[:, np.newaxis, :, :]
print(X_train.shape)
X_train = X_train[:, :, :, np.newaxis]
X_test = X_test[:, :, :, np.newaxis]
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')
print(X_train.shape)

# convert class vectors to binary class matrices using one-hot encoding method
y_train = utils.to_categorical(y_train, NB_CLASSES)
y_test = utils.to_categorical(y_test, NB_CLASSES)
model = LeNetwork.build(input_shape=INPUT_SHAPE, classes=NB_CLASSES)
model.compile(loss="categorical_crossentropy", optimizer=OPTIMIZER,
metrics=["accuracy"])
history = model.fit(X_train, y_train,
batch_size=BATCH_SIZE, epochs=NB_EPOCH,
verbose=VERBOSE, validation_split=VALIDATION_SPLIT)
score = model.evaluate(X_test, y_test, verbose=VERBOSE)

model.save("model.keras")

print("Test score:", score[0])
print('Test accuracy:', score[1])

# summarise history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# summarise history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()