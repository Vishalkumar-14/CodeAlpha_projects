import pickle
import random
import numpy as np

from tensorflow.keras.models import load_model

from music21 import stream
from music21 import note
from music21 import chord

print("Loading trained model...")

trained_model = load_model(
    "model/music_model.keras"
)

with open(
    "model/note_mapping.pkl",
    "rb"
) as mapping_file:

    saved_data = pickle.load(
        mapping_file
    )

note_to_number = saved_data[
    "note_to_number"
]

unique_notes = saved_data[
    "unique_notes"
]

number_to_note = {
    value: key
    for key, value in note_to_number.items()
}

with open(
    "notes.pkl",
    "rb"
) as notes_file:

    extracted_notes = pickle.load(
        notes_file
    )

sequence_length = 50

starting_index = random.randint(
    0,
    len(extracted_notes) - sequence_length - 1
)

seed_pattern = extracted_notes[
    starting_index:
    starting_index + sequence_length
]

network_input = [
    note_to_number[note]
    for note in seed_pattern
]

generated_notes = []

print("Generating music...")

for _ in range(200):

    prediction_input = np.reshape(
        network_input,
        (
            1,
            len(network_input),
            1
        )
    )

    prediction_input = (
        prediction_input /
        float(len(unique_notes))
    )

    prediction = trained_model.predict(
        prediction_input,
        verbose=0
    )

    predicted_index = np.argmax(
        prediction
    )

    predicted_note = number_to_note[
        predicted_index
    ]

    generated_notes.append(
        predicted_note
    )

    network_input.append(
        predicted_index
    )

    network_input = network_input[1:]

output_stream = stream.Stream()

current_offset = 0

for pattern in generated_notes:

    if "." in pattern:

        chord_notes = []

        for chord_note in pattern.split("."):

            new_note = note.Note(
                int(chord_note)
            )

            chord_notes.append(
                new_note
            )

        generated_chord = chord.Chord(
            chord_notes
        )

        generated_chord.offset = (
            current_offset
        )

        output_stream.append(
            generated_chord
        )

    else:

        generated_note = note.Note(
            pattern
        )

        generated_note.offset = (
            current_offset
        )

        output_stream.append(
            generated_note
        )

    current_offset += 0.5

output_stream.write(
    "midi",
    fp="generated_music/generated_music.mid"
)

print("Music generated successfully!")