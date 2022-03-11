import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array


def plot_example_images(plt):
    img_size = 48
    plt.figure(0, figsize=(12, 20))
    ctr = 0

    for expression in os.listdir("train_1/"):
        print(expression)
        if not expression.startswith('.DS'):
            for i in range(1, 6):
                ctr += 1
                plt.subplot(7, 5, ctr)
                path = "train_1/" + expression + "/" + \
                    os.listdir("train_1/" + expression)[i]
                img = load_img(path, target_size=(img_size, img_size))
                plt.imshow(img, cmap="gray")
            else:
                continue
    plt.tight_layout()
    return plt
