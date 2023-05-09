from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanAbsoluteError, Huber
import pandas as pd


def load_train(path):
    df = pd.read_csv(f'{path}/labels.csv')
    datagen = ImageDataGenerator(validation_split=0.25,
                                rescale=1/255,
                                rotation_range = 90,
                                horizontal_flip=True,
                                width_shift_range= .2,
                                height_shift_range = .2)
    train_datagen_flow = datagen.flow_from_dataframe(directory = f'{path}/final_files',
                                                    dataframe=df,
                                                    target_size=(244, 244),
                                                    batch_size=16,
                                                    class_mode='raw',
                                                    subset='training',
                                                    x_col = 'file_name',
                                                    y_col = 'real_age',
                                                    seed=984651)

    

    return train_datagen_flow

def load_test(path):
    df = pd.read_csv(f'{path}/labels.csv')
    test_datagen = ImageDataGenerator(validation_split=0.25,rescale=1/255)
    test_datagen_flow = test_datagen.flow_from_dataframe(directory = f'{path}/final_files',
                                                         dataframe=df,
                                                         target_size=(244,244),
                                                         batch_size=16,
                                                         class_mode='raw',
                                                         subset='validation',
                                                         x_col = 'file_name',
                                                         y_col = 'real_age',
                                                         seed=984651)

    return test_datagen_flow



def create_model(input_shape):
    backbone = ResNet50(input_shape=input_shape,
                    weights='imagenet',
                    include_top=False) 
    optimizer = Adam(lr=0.00001)
    loss = Huber()
    model = Sequential()
    model.add(backbone)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(50, activation='relu')) 
    model.add(Dense(1, activation='relu')) 
    model.compile(optimizer=optimizer, loss=loss,metrics=['mae'])
    return model


def train_model(model, train_data, test_data, batch_size=None, epochs=20,
                steps_per_epoch=None, validation_steps=None):
    model.fit(train_data,
              validation_data=test_data,
              batch_size=batch_size, epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              verbose=2)
    return model
