import io
import numpy as np
import pretty_midi
from scipy.io import wavfile

def convert_midi_to_wav(midifile):
    midi_data = pretty_midi.PrettyMIDI(midifile)
    audio_data = midi_data.fluidsynth()
    audio_data = np.int16(
        audio_data / np.max(np.abs(audio_data)) * 32767 * 0.9
    )  # -- Normalize for 16 bit audio https://github.com/jkanner/streamlit-audio/blob/main/helper.py

    virtualfile = io.BytesIO()
    wavfile.write(virtualfile, 44100, audio_data)

    return virtualfile
