from tensorflow.keras.applications import MobileNetV2             
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

base_model = MobileNetV2(input_shape=(350, 350,3),
                      include_top=False, weights="imagenet", 
                      pooling='max')
for layer in base_model.layers:
    layer.trainable = True
model_resnet = Sequential()
model_resnet.add(base_model)
model_resnet.add(Dense(4, activation='sigmoid'))
model_resnet.compile(optimizer = tf.keras.optimizers.SGD(learning_rate=0.0001), 
                     loss = 'categorical_crossentropy', 
                     metrics = ['accuracy'])
model_resnet.load_weights('../../DiseaseDetectionModels/M-Power/LungCancer/ct_resnet_best_model.hdf5')