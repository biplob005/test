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

    async_processing=True,
)

st.title("This is title")
st.write("This is body")
st.image("https://ggsc.s3.amazonaws.com/images/uploads/The_Science-Backed_Benefits_of_Being_a_Dog_Owner.jpg")
st.video("https://youtu.be/awyNVPAH_o4")

