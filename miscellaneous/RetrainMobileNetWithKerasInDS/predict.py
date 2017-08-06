from keras.applications import MobileNet
from keras.preprocessing import image
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


base_model = MobileNet(include_top=False)
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(58, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)
model.compile(optimizer=SGD(lr=0.0001, momentum=0.9), loss='categorical_crossentropy')

model.load_weights('res.h5')

labels = open('synset.txt').readlines()[:58]

def predict_img(path):
    img = load_img(path)
    x = img_to_array(img) / 255
    x = x.reshape((1, ) + x.shape)
    s = model.predict(x, 1)[0]
    return max(s), labels[s.argsort()[-1]]
