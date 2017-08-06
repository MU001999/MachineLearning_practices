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

for layer in base_model.layers:
    layer.trainable = False

model.compile(optimizer='rmsprop', loss='categorical_crossentropy')

batch_size = 20

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    'train',
    target_size=(224, 224),
    batch_size=batch_size
)

validation_generator = test_datagen.flow_from_directory(
        'test',
        target_size=(224, 224),
        batch_size=batch_size
)

model.fit_generator(
    train_generator,
    steps_per_epoch=2000 // batch_size,
    epochs = 20,
    validation_data=validation_generator,
    validation_steps=800 // batch_size
)

for layer in model.layers[:82]:
    layer.trainable = False
for layer in model.layers[82:]:
    layer.trainable = True

model.compile(optimizer=SGD(lr=0.0001, momentum=0.9), loss='categorical_crossentropy')

model.fit_generator(
    train_generator,
    steps_per_epoch=2000 // batch_size,
    epochs = 20,
    validation_data=validation_generator,
    validation_steps=800 // batch_size
)
    
model.save_weights('res.h5')

