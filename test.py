import streamlit as st
from streamlit_webrtc import webrtc_streamer

video = webrtc_streamer(key="example")
st.title("This is title")
st.write("This is body")
st.image("https://ggsc.s3.amazonaws.com/images/uploads/The_Science-Backed_Benefits_of_Being_a_Dog_Owner.jpg")
st.video("https://youtu.be/awyNVPAH_o4")

