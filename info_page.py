import streamlit as st

def info():

    st.header("Model")

    st.write("This model consists of 3-layer LSTM RNN network. It is used to capture\
    the sequence of notes from the sample music chords provided to the model.\
    We have tried catching patterns in the chords and notes, while maintaining the harmonic \
    trend of the music track, and structuring the song in a fixed temporal structure\
    We start with monophonic harmonies of a single popular instrument, in this\
    case, a PIANO. We have a list of piano midi files that can be broken down to\
    their chords and notes, and imply the char-RNN architecture on them.\
    We create a simple LSTM network that treats the midi sequences and generated\
    similar patterns for musical piece.")

    st.subheader("📻 Model Architechture")
    st.image("./src/assets/img/Model_Architechture.png", 
            caption = "Model layer arch",
            width = 500)

    st.subheader("Future Scope and Access")
    st.markdown("<ol>\
                <li>Make a Multi-track Sequential Networks for Symbolic Music Generation and Accompaniment</li>\
                <li>Generate coherent music of four bars right from scratch, without human inputs.</li>\
                <li>Given a specific track composed by a human, generate additional tracks to accompany it</li>\
                <li>Device a hybrid model for polyphonic music generation consisting of several instruments.</li>\
                <li>Creating a lyrically based generator for complex musical patterns.</li>\
                </ol>", unsafe_allow_html = True)








    st.markdown('---')
    st.caption("made by Dhruvi Shah & Visalakshi Iyer @Kaizen2k22")    