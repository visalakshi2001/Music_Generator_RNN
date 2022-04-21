import streamlit as st
from convert_midi import convert_midi_to_wav

def music():

    # st.balloons()
    st.header("Results and Demo")

    st.subheader("Piano chord visualizations")

    st.image("./src/assets/img/chords_viz.png", caption="auto generated piano-roll chords")

    st.header("🎹 Audio samples to feed the generator model")

    col1, col2 = st.beta_columns(2)

    

    with col1:
        midi_file1 = open("./music_samples/chopin_to_train/chpn-p11.mid", 'rb')
        midi_file2 = open("./music_samples/chopin_to_train/chpn_op23.mid", 'rb')
        midi_file3 = open("./music_samples/chopin_to_train/chpn_op7_1.mid", 'rb')

        if "chopin1" not in st.session_state:
            st.session_state["chopin1"] = convert_midi_to_wav(midi_file1)
        if "chopin2" not in st.session_state:
            st.session_state["chopin2"] = convert_midi_to_wav(midi_file2)
        if "chopin3" not in st.session_state:
            st.session_state["chopin3"] = convert_midi_to_wav(midi_file3)

        st.markdown("<b> Option 1:</b> <br>Classical Music by  **Chopin**:", unsafe_allow_html=True)
        st.caption("chopin live")
        st.audio(st.session_state["chopin1"], format='audio/wav')
        st.caption("chopin opera")
        st.audio(st.session_state["chopin2"], format='audio/wav')
        st.caption("chopin rendition")
        st.audio(st.session_state["chopin3"], format='audio/wav')


    with col2:
        midi_file4 = open("./music_samples/hybrid/BlueStone_LastDungeon.mid", 'rb')
        midi_file5 = open("./music_samples/hybrid/cosmo.mid", 'rb')
        midi_file6 = open("./music_samples/hybrid/figaro.mid", 'rb')

        if "hybrid1" not in st.session_state:
            st.session_state["hybrid1"] = convert_midi_to_wav(midi_file4)
        if "hybrid2" not in st.session_state:
            st.session_state["hybrid2"] = convert_midi_to_wav(midi_file5)
        if "hybrid3" not in st.session_state:
            st.session_state["hybrid3"] = convert_midi_to_wav(midi_file6)
        
        st.markdown("<b> Option 2:</b> <br>Classical Music  **Hybrid**:", unsafe_allow_html=True)
        st.caption("blueston last dungeon")
        st.audio(st.session_state["hybrid1"], format='audio/wav')
        st.caption("cosmo")
        st.audio(st.session_state["hybrid2"], format='audio/wav')
        st.caption("figaro")
        st.audio(st.session_state["hybrid3"], format='audio/wav')
    
    st.markdown('---')

    with st.form("Batch Selection"):
        st.subheader("Choose a style of music to generate synthetic version:")
        batch = st.radio('Style',
                                options=("Chopin Style", "Hybrid Style"))
        confirm = st.form_submit_button("Generate Music!")

    if confirm:
        if batch == "Chopin Style":
            with st.spinner("Generating Chopin Music"):
                with st.empty():
                    import time
                    st.image("https://c.tenor.com/UAser2NeFHkAAAAM/playing-piano-music.gif")
                    
                    output = convert_midi_to_wav(open("./music_samples/test_output_chopin.mid", 'rb'))
                    time.sleep(3.5)
                    st.balloons()
            st.subheader("Sample music generated from scratch: (Chopin)")
            st.audio(output, format="wav")

        if batch == "Hybrid Style":
            with st.spinner("Generating Hybrid Music"):
                with st.empty():
                    import time
                    st.image("https://c.tenor.com/EVKlN3Artm0AAAAC/piano-bugs-bunny.gif")
                    
                    output = convert_midi_to_wav(open("./music_samples/test_output_best.mid", 'rb'))
                    time.sleep(3.5)
                    st.balloons()
            st.subheader("✅ Sample music generated from scratch: (Hybrid)")
            st.audio(output, format="wav")
    
    st.subheader("Conclusion")
    st.write("An LSTM neural network to generate music may not be completely perfect, \
    still they are impressive in generating classical music from single instrument background. \
    This shows us that neural networks can create music and could potentially be used to help\
    create more complex musical pieces. With a better computational power, a musical GAN can \
    be created for a polygraphic musical generation network that can accompany concert artists \
    alongside their performance.")
    st.markdown('---')
    st.caption("made by Dhruvi Shah & Visalakshi Iyer @Kaizen2k22")    
