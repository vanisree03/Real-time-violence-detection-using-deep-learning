import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Mini project", page_icon=":video_camera:",layout="wide")

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open (file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)
local_css("style/style.css")

#header
with st.container():
    st.subheader("A web application for real time violence detection")
    st.title("Deep Survillence using Deep Learning :video_camera:")
    st.write("This project is an atempt to analyse real time video to detect violence")
        
lottie_coding=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_jhlaooj5.json")

with st.container():
    st.write("---")
    left_column,right_column= st.columns(2)
    with left_column:
        st.header("About the project")
        st.write("##")
        st.write(
            """
Among the widespread examples of big data, the role of video streams from CCTV cameras is equally important as other sources like social media data, sensor data, agriculture data, medical data and data evolved from space research. 
Surveillance videos have a major contribution in unstructured big data.
 Manual surveillance seems tedious and time consuming.


Automated Video Surveillance System detects an abnormality in a video using deep learning techniques.
The activities can also be detected in real-time, and these video frames will later save as an image in the system for the user to view.  
The system will detect abnormal activity with humans in the surveillance stream using an effective Spatial autoencoder.
            """
            )
        st.write("[Learn More>](https://github.com/vanisree03/Real-time-violence-detection-using-deep-learning)")
        with right_column:
         st_lottie(lottie_coding, height=300, key='coding')

with st.container():
    st.write("---")
    st.header("Do submit your reviews :")
    st.write("##")
    
    contact_form= """
    <form action="https://formsubmit.co/vanisree2k3@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Type your review here...Thank you in advance" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column =st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html =True)
    with right_column:
        st.empty()
