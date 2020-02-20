import os
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow.keras.layers as layers
import tensorflow.keras.models as models
import tensorflow.keras.optimizers as optimizers
from tensorflow.keras.models import load_model
ImageDataGenerator = tf.keras.preprocessing.image.ImageDataGenerator

base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
split_dir = os.path.join(base_dir, "SplitData")

input_shape = (500, 500, 3)


#LIMIT GPU VRAM

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    # Currently, memory growth needs to be the same across GPUs
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Memory growth must be set before GPUs have been initialized
    print(e)
# gpus = tf.config.experimental.list_physical_devices('GPU')
# if gpus:
# 	try:
# 		for gpu in gpus:
# 			tf.config.experimental.set_memory_growth(gpu, True)
# 			logical_gpus = tf.config.experimental.list_logical_devices('GPU')
# 			print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
# 	except RuntimeError as e:
# 		pass
# config = tf.ConfigProto()
# config.gpu_options.allow_growth(True)
# session = tf.Session(config=config)

# model = models.Sequential()
# model.add(layers.Conv2D(8, (3, 3), activation='relu', input_shape=input_shape))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(16, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(32, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(32, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Flatten())
# model.add(layers.Dense(128, activation='relu'))
# model.add(layers.Dense(1, activation='sigmoid'))


model = load_model('sample.h5')


train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
                        os.path.join(split_dir, "train"),
                        target_size=input_shape[0:2],
                        batch_size=20,
                        class_mode='binary')

val_generator = val_datagen.flow_from_directory(
                        os.path.join(split_dir, "val"),
                        target_size=input_shape[:2],
                        batch_size=20,
                        class_mode='binary')

test_generator = test_datagen.flow_from_directory(
                        os.path.join(split_dir, "test"),
                        target_size=input_shape[:2],
                        batch_size=20,
                        class_mode='binary')

history = model.fit_generator(
            train_generator,
            steps_per_epoch=3,
            epochs=5,
            validation_data=val_generator,
            validation_steps=2)

model.save('sample.h5')

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()
