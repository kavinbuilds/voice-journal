import streamlit as st
from datetime import datetime
import os
import whisper
from gtts import gTTS
import tempfile

st.set_page_config(page_title="voice to diary🗣️➡️📔", page_icon=":speech_balloon:", layout="centered")
#load the whisper model
@st.cache_resource
def load_model():
    return whisper.load_model("base")
model=load_model()
if "audio_key" not in st.session_state:
    st.session_state.audio_key=0
if "edit_area" not in st.session_state:
    st.session_state["edit_area"]=""
if "diary_note" not in st.session_state:
    st.session_state["diary_note"]=""
st.markdown("<h6> Voice to Diary🗣️➡️📔</h6>",unsafe_allow_html=True)

st.markdown(
        """
        <style>
        .stApp {
            background-color: #f0f0f0;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
diary_note=""
tab1,tab2=st.tabs(["**Add Diary**","**Search Diary**"])
with tab1:
    st.markdown("Upload your audio file here and convert to diary note")
    audio_file=st.audio_input("record audio",key=f"audio_input_{st.session_state.audio_key}")
    if audio_file is not None:
        with open("audio.wav","wb") as f:
            f.write(audio_file.read())
        st.audio(audio_file)
        record=st.button("clear audio",key=f"clear_audio_{st.session_state.audio_key}",type="secondary",width="stretch")
        if record:
            st.session_state.audio_key+=1
            if os.path.exists("audio.wav"):
                os.remove("audio.wav")
                st.rerun()

        if st.button("convert to diary", key="convert",type="primary",width="stretch") and audio_file is not None:
            with st.spinner("Converting voice to text... 🎙️"):
                result = model.transcribe("audio.wav")
            st.success("Conversion completed ✅")
            st.session_state["edit_area"]=result["text"]
            if st.session_state["edit_area"]:
                st.write("check the diary note...")
                edit_area=st.text_area("Your diary note", value=st.session_state["edit_area"], height=200)
                st.session_state["edit_area"]=edit_area
        #save the diary note to a text file
        if st.button("save diary note",key='save',type='primary',width="stretch"):
            os.makedirs("diary_notes", exist_ok=True)
            time=datetime.now().strftime("%d-%m-%y")
            filename=f"diary_notes/{time}.txt"
            with open(filename,'w',encoding='utf-8') as f:
                f.write(st.session_state["edit_area"])
            st.success(f"Diary note saved as {filename}")


with tab2:
    st.subheader("search by date")
    search_date=st.date_input("select date",key="search_date")
    if st.button("search",key="search",type="primary",width="stretch"):
        st.session_state["diary_note"]=""
        format_date=search_date.strftime("%d-%m-%y")
        filename=f"diary_notes/{format_date}.txt"
        if os.path.exists(filename):
            with open(filename,'r',encoding='utf-8') as f:
                st.session_state["diary_note"]=f.read()
        else:
            st.warning("no diary note found for the selected date")
    if st.session_state["diary_note"]:
        text_area=st.text_area("diary note on " + search_date.strftime("%d-%m-%y"),value=st.session_state["diary_note"],height=200)
        if st.button("🔊 Read Diary") and st.session_state["diary_note"].strip()!="":
            tts = gTTS(text=st.session_state["diary_note"], lang='en')
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                audio_file = open(fp.name, "rb")
                audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
