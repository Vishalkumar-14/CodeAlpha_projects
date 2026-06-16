import streamlit as st
import subprocess
import os

st.set_page_config(
    page_title="AI Music Generator",
    page_icon="🎵"
)

st.title("🎵 AI Music Generator")

st.write(
    "Generate simple AI-created MIDI music using "
    "patterns extracted from classical compositions."
)

st.divider()

if st.button("Generate Music"):

    subprocess.run(
        ["python", "generate_music.py"]
    )

    st.success(
        "Music generated successfully!"
    )

    music_file = (
        "generated_music/generated_music.mid"
    )

    if os.path.exists(music_file):

        with open(
            music_file,
            "rb"
        ) as file:

            st.download_button(
                label="Download MIDI File",
                data=file,
                file_name="generated_music.mid",
                mime="audio/midi"
            )

st.divider()

st.caption(
    "Developed by Vishal Kumar | CodeAlpha AI Internship"
)