import streamlit as st
import whisper
import os
import tempfile

st.title("Multi-lingual Transcription using Whisper")

audio_file = st.file_uploader("Upload your audio", type=["wav", "mp3", "m4a"])
model = whisper.load_model("base")

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing...")

        # Create a temporary file in the specified directory
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3", dir="here\temp\audio\files\output")
        temp_audio.write(audio_file.read())

        # Get the absolute path of the temporary audio file
        audio_file_path = os.path.abspath(temp_audio.name)
        st.sidebar.info("File path:", audio_file_path)

        # Ensure the temporary file is closed before removing it
        temp_audio.close()
        transcription = model.transcribe(audio_file_path)
        # Transcribe the audio
        try:
            transcription = model.transcribe(audio_file_path)
            st.sidebar.success("Transcription complete")
            st.markdown(transcription["text"])
        except Exception as e:
            st.sidebar.error(f"Error during transcription: {e}")

        # Clean up the temporary file after processing
        os.remove(audio_file_path)
    else:
        st.sidebar.error("Please upload an audio file.")
