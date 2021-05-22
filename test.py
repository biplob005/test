import streamlit as st
from streamlit_webrtc import webrtc_streamer

WEBRTC_CLIENT_SETTINGS = ClientSettings(
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": True},
)


webrtc_ctx = webrtc_streamer(
    key="audio-filter",
    mode=WebRtcMode.SENDRECV,
    client_settings=WEBRTC_CLIENT_SETTINGS,
)



