from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.layers import Conv2D, Flatten, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
import numpy as np


def load_train(path):
    features_train = np.load(path + 'train_features.npy')
    target_train = np.load(path + 'train_target.npy')
    features_train = features_train.reshape(-1, 28, 28,1) / 255.
    return features_train, target_train 


def create_model(input_shape):
    print(input_shape)
    optimizer = Adam()
    model = Sequential()
    model.add(Conv2D(filters=4, 
                     strides = 2, 
                     kernel_size=(3, 3), 
                     activation = 'relu', 
                     padding = 'same',
                     input_shape=input_shape))
    model.add(Flatten())
    """model.add(Dense(20, activation='softmax')) """
    model.add(Dense(10, activation='softmax')) 

    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy',
                  metrics=['acc'])

    return model 


def train_model(model, train_data, test_data, batch_size=32, epochs=30,
                steps_per_epoch=None, validation_steps=None):

    features_train, target_train = train_data
    features_test, target_test = test_data
    model.fit(features_train, target_train, 
              validation_data=(features_test, target_test),
              batch_size=batch_size, epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              verbose=2, shuffle=True)

    return model 