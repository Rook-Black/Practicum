from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import  mean_absolute_error as MAE


def load_train(path):
    datagen = ImageDataGenerator(validation_split=0.25, 
                                rescale=1/255,
                                rotation_range = 90,
                                horizontal_flip=True,
                                width_shift_range= .2,
                                height_shift_range = .2)
    train_datagen_flow = datagen.flow_from_directory(path,
                                                    target_size=(244, 244),
                                                    batch_size=16,
                                                    class_mode='sparse',
                                                    subset='training',
                                                    seed=984651)
    

    return train_datagen_flow

def load_test(path):
    test_datagen = ImageDataGenerator(rescale=1/255)
    test_datagen_flow = test_datagen.flow_from_directory(path,
                                                         target_size=(244,244),
                                                         batch_size=16,
                                                         class_mode='sparse',
                                                         seed=984651)

    return test_datagen_flow



def create_model(input_shape):
    backbone = ResNet50(input_shape=input_shape,
                    weights='/datasets/keras_models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5',
                    include_top=False) 
    optimizer = Adam(Ir=.0001)
    model = Sequential()
    model.add(backbone)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(12, activation='softmax')) 
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy',
                  metrics=['mae'])

    return model


def train_model(model, train_data, test_data, batch_size=None, epochs=10,
                steps_per_epoch=None, validation_steps=None):
    model.fit(train_data,
              batch_size=batch_size, epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              verbose=2)
    
    return print(model.predict(test_data))
