import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np 

#img = plt.imread("frames\\frame0.jpg")   # reading image using its name
#plt.imshow(img)
#plt.show()

data = pd.read_csv('mapping.csv')     # reading the csv file
#print(data.head())      # printing first five rows of the file

X = []     # creating an empty array
for img_name in data.Image_ID:
    img = plt.imread(f"frames\\{img_name}.jpg")
    X.append(img)  # storing each image in array X
    
X = np.array(X)    # converting list to array
