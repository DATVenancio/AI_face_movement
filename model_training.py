from keras.models import Sequential
from keras.layers import Flatten,Dense,Conv2D
from keras.applications.mobilenet_v2 import preprocess_input
from keras.preprocessing.image import img_to_array,load_img
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np
import os

DATASET_DIRECTORY = r"/home/daniel/Documents/PythonProjects/face_movement_keyboard_simulation/face_movement_keyboard_simulation/dataset"
CLASSIFICATION_CATEGORIES = ["face_down","face_idle","face_left","face_right","face_up"]



    


print("Loading images...")


data=[]
labels=[]

for category in CLASSIFICATION_CATEGORIES:
    category_path = os.path.join(DATASET_DIRECTORY,category)
    for item in os.listdir(category_path):
        image_path = os.path.join(category_path,item)
        image = load_img(image_path,target_size=(224,224))
        image = img_to_array(image)
        image = preprocess_input(image)

        data.append(image)
        labels.append(category)
print("Loaded")
labels = LabelEncoder().fit_transform(labels)
labels = to_categorical(labels,num_classes=5)


data = np.array(data, dtype="float32")
labels = np.array(labels)

(train_images,test_images,train_labels,test_labels) =  train_test_split(data,labels,test_size=0.50)




model = Sequential()

model.add(Conv2D(
    input_shape=(224, 224, 3),
    filters=24, 
    kernel_size=(1,1), 
    activation='relu')
)
model.add(Flatten())
model.add(Dense(5, activation='softmax'))

model.summary()
     


LOSS = 'categorical_crossentropy'
OPTIMIZER = 'adam'

model.compile(optimizer=OPTIMIZER,
              loss=LOSS,
              metrics=['accuracy'])
     
NUM_EPOCHS = 10




history = model.fit(
                    train_images, train_labels,
                    epochs=NUM_EPOCHS, 
                    validation_data=(test_images,test_labels)
)
     
model.save("face_movement.model",save_format="h5")
     
