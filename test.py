import streamlit as st
from streamlit_webrtc import (
    AudioProcessorBase,
    ClientSettings,
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer,
)




webrtc_ctx = webrtc_streamer(
    key="audio-filter",
    mode=WebRtcMode.SENDRECV
)



