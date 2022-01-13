import numpy as np
import pandas as pd 
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from PIL import Image
import PIL.ImageOps 
X,y=fetch_openml('mnist_784',version=1,return_X_y=True)
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=7500,test_size=2500,random_state=9)
x_trainscale=X_train/255
x_testscale=X_test/255
clf=LogisticRegression(solver="saga",multi_class="multinomial")
clf.fit(x_trainscale,y_train)
def get_prediction(image):
    im_pil=Image.open(image)
    im_bw=im_pil.convert("L")
    im_bw_resized=im_bw.resize((28,28),Image.ANTIALIAS)
    pixel_filter=20
    min_pixel=np.percentile(im_bw_resized,pixel_filter)
    img_bw_resized_inverted_scaled=np.clip(im_bw_resized - min_pixel,0,255)
    max_pixel=np.max(im_bw_resized)
    img_bw_resized_inverted_scaled=np.asarray(img_bw_resized_inverted_scaled)/max_pixel
    testSample=np.array(img_bw_resized_inverted_scaled).reshape(1,784)
    prediction=clf.predict(testSample)
    return prediction[0]
    












