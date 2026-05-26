import streamlit as st
from datetime import datetime
import os
import whisper
#load the whisper model
model=whisper.load_model("base")
st.set_page_config(page_title="voice to diary🗣️➡️📔", page_icon=":speech_balloon:", layout="centered")
st.markdown("<h6> Voice to Diary🗣️➡️📔</h6>",unsafe_allow_html=True)
st.text("Upload your audio file here and convert to diary note")
st.markdown(
        """
        <style>
        .stApp {
            background-color: navy-blue;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
audio_file=st.file_uploader("upload your audio file here",type=['mp3','wav', 'm4a'])
if audio_file is not None:
    with open("audio.mp3","wb") as f:
        f.write(audio_file.read())
    st.audio(audio_file)

    if st.button("convert to diary", key="convert",type="primary",use_container_width=True,width="stretch"):
        result=model.transcribe("audio.mp3")
        st.session_state["edit_area"]=result["text"]
        edit_area=st.text_area("Your diary note", value=st.session_state["edit_area"], height=200)
    #save the diary note to a text file
        if st.button("save diary note",key='save',type='primary'):
            os.makedirs("diary_notes", exist_ok=True)
            time=datetime.now().strftime("%d-%m-%y")
            filename=f"diary_notes/{time}.txt"
            edit_area=st.text_area("Your diary note", value=st.session_state["edit_area"], height=200)
            with open(filename,'w',encoding='utf-8') as f:
                st.write("check the diary note...")
                f.write(edit_area)
            st.success(f"Diary note saved as {filename}")

with st.sidebar:
    st.subheader("search by date")
    search_date=st.date_input("select date",key="search_date")
    if st.button("search",key="search",type="primary",use_container_width=True,width="stretch`"):
        format_date=search_date.strftime("%d-%m-%y")
        filename=f"diary_notes/{format_date}.txt"
        if os.path.exists(filename):
            with open(filename,'r',encoding='utf-8') as f:
                diary_note=f.read()
                if diary_note:
                    st.text_area("diary note",value=diary_note,height=200)
        else:
            st.warning("no diary note found for the selected date")