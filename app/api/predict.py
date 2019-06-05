import skimage
from skimage.transform import resize
import os
import numpy as np
import json
import requests
from matplotlib import pyplot as plt

def show_image(X):
    plt.imshow(np.squeeze(X), cmap="gray")
    plt.show()

IMG_SIZE = 160
path = './../static/dataset_test'
## FAILED
# img = '0004.jpg'
# img = 'B0tLsXHCYAAAeq-.jpg'
# img = 'DwX7Vz9uVgdx_HqV0-gefJ4FI8btsuB3BmmtrgCIvi4.jpg'
# img = 'fsc.jpg'

## GOOD
path = './../static/dataset_test/good'
# img = '5e04faf6b1ebee0735ffb82771ca9051_preview_featured.jpg'
img = 'BV-Acharya-9.jpg'
# img = 'fused-filament-fabrication-fff-thumb-600x300.jpg'
# img = 'index.jpg'




image = skimage.io.imread(os.path.join(path, img))
image = resize(image, (IMG_SIZE, IMG_SIZE))

# If grayscale. Convert to RGB for consistency.
# print(image.ndim)
# if image.ndim != 3:
#     image = skimage.color.gray2rgb(image)

# image = 1 - np.array(image).astype('float32') / 255.
# image = image/255
# image = 1 - np.array(image).astype('float32')
# show_image(image)


# data = json.dumps({"signature_name": "serving_default", "instances": image[0:3].tolist()})
data = json.dumps({"signature_name": "serving_default", "instances": [image.tolist()]})


headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/half_plus_two:predict', data=data, headers=headers)
# predictions = json.loads(json_response.text)['predictions']
predictions = json.loads(json_response.text)

print(predictions)
print(json_response)