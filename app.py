import streamlit as st

# This MUST be the first Streamlit command
st.set_page_config(page_title="Ingunn Tonetta Erdal")

# Define pages
home_page = st.Page("home.py", title="About me", icon="👋")
experience_page = st.Page("experience.py", title="Experience", icon="💼")
projects_page = st.Page("projects.py", title="Projects", icon="🎨")
competitions_page = st.Page("competitions.py", title="Competitions", icon="🏆")

# Create navigation
pg = st.navigation([home_page, experience_page, projects_page, competitions_page])

# Run the selected page
pg.run()


