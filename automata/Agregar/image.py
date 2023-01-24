import streamlit as st
from PIL import Image

image1 = Image.open('img\photo_2023-01-24_08-58-08.jpg')
st.image(image1, caption='With Immunity, Time:305  Gen:5',width=400)
image2 = Image.open('img\photo_2023-01-24_08-58-37.jpg')
st.image(image2, caption='With Immunity, Time:3455  Gen:24',width=400)
image3 = Image.open('img\photo_2023-01-24_08-58-43.jpg')
st.image(image3, caption='With Immunity, Time:4225  Gen:40',width=400)
image4 = Image.open('img\photo_2023-01-24_08-58-50.jpg')
st.image(image4, caption='With Immunity, Time:6220  Gen:55',width=400)