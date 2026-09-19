import streamlit as st

# This MUST be the first Streamlit command
st.set_page_config(page_title="Ingunn Tonetta Erdal")

# Move navigation bar and hide deploy button
st.markdown(
    """
    <style>
    /* Hide all action buttons and menus */
    button[kind="header"],
    [data-testid="stStatusWidget"],
    #MainMenu,
    header button {
        display: none !important;
    }

    /* Move the toolbar 100px to the right */
    [data-testid="stToolbar"] {
        margin-left: 575px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define pages
home_page = st.Page("pages/home.py", title="About me", icon="👋")
education_page = st.Page("pages/education.py", title="Education", icon="🎓")
experience_page = st.Page("pages/experience.py", title="Experience", icon="💼")
projects_page = st.Page("pages/projects.py", title="Projects", icon="💻")
competitions_page = st.Page("pages/competitions.py", title="Competitions", icon="🏆")

# Create navigation
pg = st.navigation([home_page, education_page, experience_page, projects_page, competitions_page], position="top")

# Run the selected page
pg.run()


