import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

# load save model
model_fraud = pickle.load(open('model_fraud.sav','rb'))

tfidf = TfidfVectorizer

loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(pickle.load(open("new_selected_feature_tf-idf.sav", "rb"))))

# judul halaman
st.title ('prediksi sms penipuan')

clean_teks = st.text_input('masukan teks sms')

fraud_detection = ''

if st.button('hasil deteksi') :
    predict_fraud = model_fraud.predict(loaded_vec.fit_transform([clean_teks]))

    if (predict_fraud == 0):
        fraud_detection = 'sms normal'
    elif (predict_fraud == 1):
        fraud_detection = 'sms fraud'
    else :
        fraud_detection ='sms promo'

st.success(fraud_detection)

clean_teks = st.text_input('TUGAS SKRIPSI DWI MUHAMAD HISYAM')
