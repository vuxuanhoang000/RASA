from glob import glob
import numpy as np
import tensorflow as tf
from keras.applications.resnet import preprocess_input
from keras.applications.resnet import ResNet50
from PIL import Image
import requests
from io import BytesIO
from extract_bottleneck_features import *

dog_names = [
    item[20:-1].replace("_", " ").replace("-", " ").lower()
    for item in sorted(glob("dogImages/train/*/"))
]
CLASS_NUM = len(dog_names)


def create_model():
    from keras.layers import Dense, GlobalAveragePooling2D
    from keras.models import Sequential

    model = Sequential()
    model.add(GlobalAveragePooling2D(input_shape=(7, 7, 2048)))
    model.add(Dense(CLASS_NUM, activation="softmax"))
    return model


model = create_model()
model.load_weights("saved_models/weights.best_adamax.ResNet50.hdf5")


def path_to_tensor(img_path):
    if img_path.startswith("http"):
        response = requests.get(img_path)
        img = Image.open(BytesIO(response.content)).resize((224, 224))
    else:
        img = tf.keras.utils.load_img(img_path, target_size=(224, 224))
    x = tf.keras.utils.img_to_array(img)
    return np.expand_dims(x, axis=0)


ResNet50_model = ResNet50(weights="imagenet")


def ResNet50_predict_labels(img_path):
    img = preprocess_input(path_to_tensor(img_path))
    return np.argmax(ResNet50_model.predict(img))


def dog_detector(img_path):
    prediction = ResNet50_predict_labels(img_path)
    return (prediction <= 268) & (prediction >= 151)


def ResNet50_predict_breed(img_path):
    bottleneck_feature = extract_Resnet50(path_to_tensor(img_path))
    predicted_vector = model.predict(bottleneck_feature)
    return dog_names[np.argmax(predicted_vector)]


def predict_breed(img_path):
    is_dog = dog_detector(img_path)
    return ResNet50_predict_breed(img_path) if is_dog else None


print(
    predict_breed(
        r"D:\VsCode\RASA\Dog-Breed-Classifier-Chatbot\dogImages\test\003.Airedale_terrier\Airedale_terrier_00166.jpg"
    )
)
