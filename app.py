import streamlit as st 
import os 
from PIL import Image 
import pickle
import numpy as np 
from tensorflow.keras.preprocessing import image
from numpy.linalg import norm
from tensorflow.keras.applications.resnet50 import preprocess_input
from sklearn.neighbors import NearestNeighbors
import cv2
import joblib

model = joblib.load('src/artifacts/prepare_base_model/base_model.joblib')


dir_file = 'src/artifacts/data_preprocessing/'
data_img_path = 'src/artifacts/data_ingestion/'

embeddings_file_path = os.path.join(dir_file,'embeddings.pkl')
# print(embeddings_file_path)
feature_list = np.array(pickle.load(open(embeddings_file_path,'rb')))

filenames_path = os.path.join(dir_file,'filenames.pkl')
# print(filenames_path)
filenames = pickle.load(open(filenames_path,'rb'))


st.title("Visual Search & Image Recognition")

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('uploads',uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1
    except:
        return 0
    
def feature_extraction(img_path,model):
    img = image.load_img(img_path,target_size=(224,224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0) # here imgs are being converted in batches
    preprocessed_img = preprocess_input(expanded_img_array)
    result = model.predict(preprocessed_img).flatten()
    normalized_result = result / norm(result)
    return normalized_result

def recommend(features,feature_list):
    neighbors = NearestNeighbors(n_neighbors=6,algorithm='brute',metric='euclidean')
    neighbors.fit(feature_list)
    distances,indices = neighbors.kneighbors([features])
    return indices


uploaded_file = st.file_uploader("Choose an image")
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        display_image = Image.open(uploaded_file)
        st.image(display_image)

        features = feature_extraction(os.path.join("uploads",uploaded_file.name),model)
        indices = recommend(features,feature_list)

        col1,col2,col3,col4,col5 = st.columns(5)

        with col1:
            st.image(Image.open(os.path.join(data_img_path, filenames[indices[0][0]].replace('\\', '/'))))
        with col2:
            st.image(Image.open(os.path.join(data_img_path, filenames[indices[0][1]].replace('\\', '/'))))
        with col3:
            st.image(Image.open(os.path.join(data_img_path, filenames[indices[0][2]].replace('\\', '/'))))
        with col4:
            st.image(Image.open(os.path.join(data_img_path, filenames[indices[0][3]].replace('\\', '/'))))
        with col5:
            st.image(Image.open(os.path.join(data_img_path, filenames[indices[0][4]].replace('\\', '/'))))


    else:
        st.header("Some error occured in the file upload")