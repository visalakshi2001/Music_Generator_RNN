import glob
import pickle
from music21 import converter, instrument, note, chord, stream

def get_notes(filename):
    """ Get all the notes and chords from the midi files in the ./midi_songs directory """
    notes = []
    # start parsing each song file in folder
    for file in glob.glob(filename):
        midi = converter.parse(file)

        print("Parsing %s" % file)
        pick = None
        songs = instrument.partitionByInstrument(midi)
        # start parsing every instrument part of song-file 
        for part in songs.parts:
            pick = part.recurse()
            # start parsing every element of instrument
            for element in pick:
                if len(sorted(set(item for item in notes))) == 279:
                    break
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append(".".join(str(n) for n in element.normalOrder))
    # end parsing each song file in folder
    
    print(f"Generated input list of length {len(set(item for item in notes))}")
    
    # check & extend input length to match the model (this part is improvised)
    if len(set(item for item in notes)) < 279:
        print(f"Sampling from reserve to complete input file")
        with open(r'./assets/notes', 'rb') as filepath:
            res = pickle.load(filepath)
        r = list(set(item for item in res if item not in notes))
        notes.extend(r[:279-len(set(notes))])
    # end of custom extension (this part is improvised)    
    
    with open(r'./assets/notes_custom', 'wb') as filepath:
        pickle.dump(notes, filepath)
    
    print(f"Generated notelist of length {len(notes)}")
    print(f"Generated input list of length {len(set(item for item in notes))}")
    return notes