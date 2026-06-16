# 🎵 AI Music Generation System

## Overview

This project was developed as part of the CodeAlpha Artificial Intelligence Internship Program.

The AI Music Generation System uses Deep Learning techniques to generate new musical compositions based on patterns learned from classical music. The project utilizes the `music21` library for music preprocessing and an LSTM (Long Short-Term Memory) neural network built using TensorFlow and Keras for sequence learning.

The model is trained on musical note sequences extracted from Bach compositions available in the music21 corpus. After training, the model generates new note patterns which are converted into MIDI files that can be played using any MIDI-compatible software.

---

## Features

* Extracts musical notes and chords from classical compositions
* Preprocesses music data into sequential patterns
* Trains an LSTM Neural Network for music generation
* Generates new music based on learned note sequences
* Exports generated music as MIDI files
* Interactive Streamlit web interface
* Download generated MIDI files directly from the application

---

## Technologies Used

* Python
* TensorFlow
* Keras
* Music21
* NumPy
* Streamlit

---

## Project Structure

```text
CodeAlpha_MusicGenerationAI/
│
├── app.py
├── preprocess.py
├── train_model.py
├── generate_music.py
├── requirements.txt
├── README.md
│
├── notes.pkl
│
├── model/
│   ├── music_model.keras
│   └── note_mapping.pkl
│
├── generated_music/
│   └── generated_music.mid
│
├── screenshots/
│
└── dataset_info/
```

---

## Workflow

### 1. Music Data Collection

The project uses Bach compositions from the built-in music21 corpus as the training dataset.

### 2. Data Preprocessing

Musical notes and chords are extracted from the compositions and stored in a serialized format (`notes.pkl`) for training.

### 3. Model Training

An LSTM Neural Network is trained on the extracted note sequences to learn musical patterns and relationships between notes.

### 4. Music Generation

The trained model predicts the next note in a sequence repeatedly to generate a completely new musical composition.

### 5. MIDI Export

Generated notes are converted into a MIDI file that can be downloaded and played using external applications.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Vishalkumar-14/CodeAlpha_projects.git
```

Navigate to the project folder:

```bash
cd CodeAlpha_MusicGenerationAI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Step 1: Preprocess Music Data

```bash
python preprocess.py
```

### Step 2: Train the Model

```bash
python train_model.py
```

### Step 3: Generate Music

```bash
python generate_music.py
```

### Step 4: Launch the Web Application

```bash
streamlit run app.py
```

---

## Model Architecture

The music generation model uses:

* LSTM Layer (256 Units)
* Dropout Layer (0.3)
* LSTM Layer (256 Units)
* Dropout Layer (0.3)
* Dense Layer (128 Units)
* Softmax Output Layer

This architecture enables the model to learn sequential musical patterns and generate coherent note sequences.

---

## Results

* Extracted over 3900 musical notes from classical compositions.
* Successfully trained an LSTM-based music generation model.
* Generated new MIDI music files from learned note patterns.
* Built an interactive interface for easy music generation and download.

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Sequence Modeling
* Recurrent Neural Networks (RNNs)
* Long Short-Term Memory Networks (LSTMs)
* Music Data Processing
* Deep Learning with TensorFlow
* Building AI-powered applications using Streamlit

---

## Future Improvements

* Train on larger MIDI datasets
* Add genre selection
* Support multiple instruments
* Improve melody diversity
* Deploy the application online
* Add real-time audio playback

---

## Author

**Vishal Kumar**

B.Tech CSE (AI & ML)
Graphic Era Deemed to be University

Developed as part of the **CodeAlpha Artificial Intelligence Internship Program**.
