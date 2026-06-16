import streamlit as st
import subprocess
import os

st.set_page_config(
    page_title="AI Music Generator",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 AI Music Generator")

st.write(
    """
    Generate original MIDI music using an LSTM Neural Network
    trained on classical Bach compositions.

    Click the button below to create a new music file.
    """
)

st.divider()

if st.button("Generate Music"):

    with st.spinner("Generating music..."):

        subprocess.run(
            ["python", "generate_music.py"]
        )

    midi_file_path = (
        "generated_music/generated_music.mid"
    )

    if os.path.exists(midi_file_path):

        st.success(
            "Music generated successfully!"
        )

        with open(
            midi_file_path,
            "rb"
        ) as midi_file:

            st.download_button(
                label="Download MIDI File",
                data=midi_file,
                file_name="generated_music.mid",
                mime="audio/midi"
            )

st.divider()

st.subheader("Project Details")

st.markdown("""
- Model: LSTM Neural Network
- Dataset: music21 Bach Corpus
- Framework: TensorFlow / Keras
- Output: MIDI Music File
""")

st.caption(
    "Developed by Vishal Kumar | CodeAlpha AI Internship"
)