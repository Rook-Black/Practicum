from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.layers import Conv2D, Flatten, Dense, AveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np



def load_train(path):

    train_datagen = ImageDataGenerator(validation_split=0.25, 
                                   rescale=1/255.)
    
    train_datagen_flow = train_datagen.flow_from_directory(path,
                                                            target_size=(150,150),
                                                            batch_size=16,
                                                            class_mode='sparse',
                                                            subset='training',
                                                            seed=12345)

                                                                
    return train_datagen_flow


def create_model(input_shape):
    optimizer = Adam()
    model = Sequential()
    model.add(Conv2D(filters=6,
                     kernel_size=(3, 3), 
                     activation = 'relu', 
                     input_shape=input_shape))
    model.add(AveragePooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(12, activation='softmax')) 

    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy',
                  metrics=['acc'])

    return model 


def train_model(model, train_data, test_data, batch_size=1, epochs=1,
                steps_per_epoch=1, validation_steps=1):


    model.fit(train_data,
              validation_data=test_data,
              batch_size=batch_size, epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              verbose=2, shuffle=True)

    return model 