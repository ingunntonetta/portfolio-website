import streamlit as st
from footer import footer

st.title("Ingunn Tonetta Erdal", text_alignment="center")

st.subheader("About me", text_alignment="center")

st.markdown("""
    I'm a fifth-year **cybersecurity** student at NTNU in Trondheim. Internships at **Norsk Hydro** and **NTE Telekom** have given me
    practical experience in both **OT and IT security**.Outside of my studies, I **lead an AI project** focused on proactive,
    offensive security, and I work as a student assistant for a network
    management course at NTNU.
    """, text_alignment="center")

st.image("images/meg.png") 

st.subheader("Contact me", text_alignment="center")

with st.form("contact_form"):

    name = st.text_input("Name",placeholder="email")

    message = st.text_area("Message",placeholder="your message")

    submitted = st.form_submit_button("Send message")

    if submitted:
        st.success("Thanks for your message! 👋")

footer()