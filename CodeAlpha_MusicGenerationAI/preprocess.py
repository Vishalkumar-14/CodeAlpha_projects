from music21 import corpus
from music21 import note
from music21 import chord
from music21 import instrument
import pickle

all_notes = []

training_songs = [
    "bach/bwv66.6",
    "bach/bwv67.4",
    "bach/bwv69.6",
    "bach/bwv277"
]

print("Starting music preprocessing...\n")

for song_name in training_songs:

    print(f"Processing {song_name}")

    current_song = corpus.parse(song_name)

    song_parts = instrument.partitionByInstrument(current_song)

    if song_parts:
        notes_to_parse = song_parts.parts[0].recurse()
    else:
        notes_to_parse = current_song.flatten().notes

    for music_element in notes_to_parse:

        if isinstance(music_element, note.Note):
            all_notes.append(str(music_element.pitch))

        elif isinstance(music_element, chord.Chord):
            chord_notes = ".".join(
                str(single_note)
                for single_note in music_element.normalOrder
            )

            all_notes.append(chord_notes)

print(f"\nTotal notes collected: {len(all_notes)}")

with open("notes.pkl", "wb") as notes_file:
    pickle.dump(all_notes, notes_file)

print("notes.pkl created successfully!")