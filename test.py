
import streamlit as st

from streamlit_webrtc import webrtc_streamer
st.title('hello world')
video = webrtc_streamer(key="example")
print(type(video))


