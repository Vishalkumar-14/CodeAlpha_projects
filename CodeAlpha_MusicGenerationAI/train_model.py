import pickle
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.utils import to_categorical

print("Loading extracted notes...")

with open("notes.pkl", "rb") as notes_file:
    extracted_notes = pickle.load(notes_file)

print(f"Total notes loaded: {len(extracted_notes)}")

unique_notes = sorted(set(extracted_notes))

note_to_number = {
    note_value: number
    for number, note_value in enumerate(unique_notes)
}

sequence_length = 50

network_inputs = []
network_outputs = []

for index in range(
    0,
    len(extracted_notes) - sequence_length
):

    input_sequence = extracted_notes[
        index:index + sequence_length
    ]

    output_note = extracted_notes[
        index + sequence_length
    ]

    network_inputs.append(
        [note_to_number[note] for note in input_sequence]
    )

    network_outputs.append(
        note_to_number[output_note]
    )

total_patterns = len(network_inputs)

print(f"Training patterns: {total_patterns}")

network_inputs = np.reshape(
    network_inputs,
    (
        total_patterns,
        sequence_length,
        1
    )
)

network_inputs = network_inputs / float(
    len(unique_notes)
)

network_outputs = to_categorical(
    network_outputs
)

print("Building LSTM model...")

music_model = Sequential()

music_model.add(
    LSTM(
        256,
        input_shape=(
            network_inputs.shape[1],
            network_inputs.shape[2]
        ),
        return_sequences=True
    )
)

music_model.add(
    Dropout(0.3)
)

music_model.add(
    LSTM(256)
)

music_model.add(
    Dropout(0.3)
)

music_model.add(
    Dense(128, activation="relu")
)

music_model.add(
    Dense(
        len(unique_notes),
        activation="softmax"
    )
)

music_model.compile(
    loss="categorical_crossentropy",
    optimizer="adam"
)

print("Starting training...")

music_model.fit(
    network_inputs,
    network_outputs,
    epochs=25,
    batch_size=64
)

music_model.save(
    "model/music_model.keras"
)

with open(
    "model/note_mapping.pkl",
    "wb"
) as mapping_file:

    pickle.dump(
        {
            "note_to_number": note_to_number,
            "unique_notes": unique_notes
        },
        mapping_file
    )

print("Model training completed!")
print("Model saved successfully!")