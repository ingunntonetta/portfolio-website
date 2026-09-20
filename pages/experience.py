import streamlit as st
from footer import footer

# Hide video controls and style logos
st.markdown("""
<style>
/* Hide all video controls */
video::-webkit-media-controls {
    display: none !important;
}
video::-webkit-media-controls-enclosure {
    display: none !important;
}
video::-webkit-media-controls-panel {
    display: none !important;
}
video {
    pointer-events: none !important;
}

</style>
""", unsafe_allow_html=True)

st.title(" Work Experience", text_alignment="center")

st.subheader("Related work")

date_col, text_col, image_col = st.columns([1, 4, 2])

with date_col:
    st.markdown("**2026**")
    st.write("*Jun - Aug*")

with text_col:
    st.markdown("**Summer internship**")
    st.write("*Norsk Hydro*")
    st.write("Description of your role and responsibilities. What you accomplished and learned during this position.")


with image_col:
    st.image("images/meg_og_helmer.png")


#image_col, video_col, image_2_col = st.columns([1, 1, 1])

#with image_col:
    #st.image("images/meg_hydro.png")

#with video_col:
    #st.video("images/hydro_video.mov", autoplay=True, muted=True, loop=True)

#with image_2_col:
    #st.image("images/alle_hydro.jpg")


date_col, text_col, image_col = st.columns([1, 4, 2])

with date_col:
    st.markdown("**2025**")
    st.write("*Jun - Aug*")

with text_col:
    st.markdown("**Summer internship**")
    st.write("*NTE Telekom*")
    st.write("Description of your role and responsibilities. What you accomplished and learned during this position.")

with image_col:
    st.image("images/meg_nte.jpg")

date_col, text_col, image_col = st.columns([1, 4, 2])

with date_col:
    st.markdown("**2025**")
    st.write("*Jun - Aug*")

with text_col:
    st.markdown("**Programming teacher**")
    st.write("*YoungCoderz*")
    st.write("Description of your role and responsibilities. What you accomplished and learned during this position.")

with image_col:
    st.image("images/youngcoders.png")


st.subheader("Volunteer work")

date_col, text_col, empty_col, logo_col = st.columns([1, 4, 1, 1])

with date_col:
    st.markdown("**2024-Present**")
    st.write("*Jan - Now*")

with text_col:
    st.markdown("**Member**")
    st.write("*Itemize NTNU*")
    st.write("Practical experience with offensive security through CTF competitions and ethical hacking courses.")

with empty_col:
    st.write("")

with logo_col:
    st.image("images/itemize.jpeg")

date_col, text_col, empty_col, logo_col = st.columns([1, 4, 1, 1])

with date_col:
    st.markdown("**2025-2026**")
    st.write("*Oct - Jun*")

with text_col:
    st.markdown("**Partnerships Coordinator**")
    st.write("*Sikkerhetspolitisk Dag (SPD)*")
    st.write("Multi-day conference on how state actors attempt to influence Norwegian democracy through cyber operations and other means.")

with empty_col:
    st.write("")

with logo_col:
    st.image("images/spd.jpeg")

date_col, text_col, empty_col, logo_col = st.columns([1, 4, 1, 1])

with date_col:
    st.markdown("**2022-2024**")
    st.write("*Aug - Jun*")

with text_col:
    st.markdown("**Marketing and Promotion**")
    st.write("*Linjeforeningen TIHLDE*")
    st.write("Promoted events through social media and the website. Created visual materials, including posters, graphics, and logos.")

with empty_col:
    st.write("")

with logo_col:
    st.image("images/thilde.jpeg")


date_col, text_col, empty_col, logo_col = st.columns([1, 4, 1, 1])

with date_col:
    st.markdown("**2023**")
    st.write("*Apr - Dec*")

with text_col:
    st.markdown("**Bar Manager**")
    st.write("*UKA*")
    st.write("Leader for a group of 20 people at Norway's largest culture festival.")

with empty_col:
    st.write("")

with logo_col:
    st.image("images/uka.png")




footer()