import streamlit as st
import speech_recognition as sr
st.title("speech Recognition")
def takecomand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Recognizing....")
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            st.text_area("You  said :",text,height=200)
        except:
            st.write("Please say again ..")
        return text

if st.button("Click me"):
    takecomand()