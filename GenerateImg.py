import keras_cv
from tensorflow import keras

import matplotlib.pyplot as plt


model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)


def plot_images(images):
    plt.figure(figsize=(20, 20))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.axis("off")
        
images = model.text_to_image(
    "Paris in Heaven, fantasy art, "
    "light blue color, high quality, highly detailed, elegant, sharp focus, "
    "concept art, character concepts, digital painting, mystery, adventure",
    batch_size=3,
)
plot_images(images)
