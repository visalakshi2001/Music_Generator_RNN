import streamlit as st

def abstract():
    st.image("https://images.unsplash.com/photo-1479118013749-9f79d55a28d0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80")

    st.header("Abstract")
    st.write("Generating music has a few notable differences from generating images and videos. \
    First, music is an art of time, necessitating a temporal model. Second, music is usually composed \
    of multiple instruments/tracks with their own temporal dynamics, but collectively they unfold \
    over time interdependently. Lastly, musical notes are often grouped into chords, arpeggios, \
    or melodies in polyphonic music, and thereby introducing a chronological ordering of notes \
    is not naturally suitable. In recent years, there has been efforts to generate art styles like \
    text production, video production and consequently music production. This involves starting with \
    producing music from single notes, multi-note chorus music from concerts, etc. In this project, \
    we focus upon producing monophonic music from a single instrument (majorly classical piano tunes) \
    and aim to achieve a seamless synthetic generation of music with recurrent neaural network.")

    st.markdown("**Keywords:** RNN, music generator, piano, deep learning")
    st.subheader("Listen to the best sample yet: (7000 iteration)")
    with st.beta_columns(2)[0]:
        st.audio(open("./music_samples/home_demo.mp3", 'rb').read(), format='audio/mp3')
    st.markdown('---')
    st.caption("made by Dhruvi Shah & Visalakshi Iyer @Kaizen2k22")    