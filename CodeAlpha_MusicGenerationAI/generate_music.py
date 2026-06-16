import pickle
import random
from music21 import stream
from music21 import note
from music21 import chord

with open("notes.pkl", "rb") as notes_file:
    all_notes = pickle.load(notes_file)

generated_melody = []

starting_index = random.randint(
    0,
    len(all_notes) - 101
)

current_pattern = all_notes[
    starting_index:starting_index + 100
]

for _ in range(100):

    next_note = random.choice(current_pattern)

    generated_melody.append(next_note)

output_stream = stream.Stream()

current_offset = 0

for pattern in generated_melody:

    if "." in pattern or pattern.isdigit():

        notes_in_chord = pattern.split(".")

        chord_notes = []

        for single_note in notes_in_chord:

            new_note = note.Note(int(single_note))
            chord_notes.append(new_note)

        new_chord = chord.Chord(chord_notes)
        new_chord.offset = current_offset

        output_stream.append(new_chord)

    else:

        new_note = note.Note(pattern)
        new_note.offset = current_offset

        output_stream.append(new_note)

    current_offset += 0.5

output_stream.write(
    "midi",
    fp="generated_music/generated_music.mid"
)

print("Music generated successfully!")