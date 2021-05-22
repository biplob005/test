import streamlit as st
from streamlit_webrtc import webrtc_streamer

video = webrtc_streamer(key="example")
st.title("This is title")
st.write("This is body")
