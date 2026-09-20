import streamlit as st
from footer import footer

st.title("Projects", text_alignment="center")

st.markdown("""
    Take a look at my homade projects. 
    """, text_alignment="center")

projects = [
    {
        "title": "RegulAId",
        "description": "AI project to help organisations comply with EU AI Act. Chatbot with RAG and agents.",
        "tags": ["Web","AI"],
        "github": "https://github.com/CogitoNTNU/RegulAId",
        "media": "images/regulAId_video.mov",
        "media_type": "video",
    },
    {
        "title": "Sovereign AI",
        "description": "AI chatbot integrated with Microsoft's Sovereign Landing Zone.",
        "tags": ["AI", "Cloud", "Cybersecurity"],
        "github": "https://github.com/ingunntonetta/bachelor-thesis-2025",
        "media": "images/query_average_salary.png",
        "media_type": "image",
    },
    {
        "title": "Jeopardy Game",
        "description": "Simple Jeopardy game built with React and TypeScript.",
        "tags": ["Web", "Cloud"],
        "github": "https://github.com/ingunntonetta/jeopardy-game",
        "media": "images/jeopardy.png",
        "media_type": "image",
    },
    {
        "title": "Test Automation Agents",
        "description": "Browser-based agents to automate both test creation and test execution in ERP system.",
        "tags": ["Web", "AI"],
        "github": "https://github.com/CogitoNTNU/cogitoxinfor-agents",
        "media": "images/jeopardy.png",
        "media_type": "image",
    },
]

# Filter
all_tags = sorted({
    tag
    for project in projects
    for tag in project["tags"]
})

# Center the filter pills and fix image sizes
st.markdown("""
<style>
div[data-testid="stPills"] > div {
    justify-content: center;
    gap: 8px;
}

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

/* Make project boxes wider */
.wider-projects {
    max-width: 1400px !important;
    margin: 0 auto;
}

/* Target all images on the projects page directly */
[data-testid="stImage"] {
    height: 200px !important;
    min-height: 200px !important;
    max-height: 200px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    overflow: hidden !important;
}

[data-testid="stImage"] img {
    height: 200px !important;
    max-height: 200px !important;
    width: auto !important;
    max-width: 100% !important;
    object-fit: contain !important;
    object-position: center !important;
}

/* Fix video height too */
video {
    height: 200px !important;
    max-height: 200px !important;
    object-fit: contain !important;
}

/* Force all bordered containers to same minimum height */
div[style*="border"] {
    min-height: 520px !important;
}
</style>
""", unsafe_allow_html=True)


# Filter
selected_tag = st.pills(
    "Filter",
    ["All"] + all_tags,
    default="All",
    label_visibility="collapsed",
    width="stretch"
)


# Filter projects
if selected_tag == "All":
    filtered_projects = projects
else:
    filtered_projects = [
        project
        for project in projects
        if selected_tag in project["tags"]
    ]


# Display two projects per row
st.markdown('<div class="wider-projects">', unsafe_allow_html=True)
for i in range(0, len(filtered_projects), 2):

    col1, col2 = st.columns(2)

    with col1:
        project = filtered_projects[i]

        with st.container(border=True):
            if project.get("media_type") == "video":
                st.video(project["media"], autoplay=True, muted=True, loop=True)
            else:
                st.image(project["media"], use_container_width=True)
            st.subheader(project["title"])
            st.write(project["description"])

            st.link_button(
                "GitHub ↗",
                project["github"],
                use_container_width=True
            )

    if i + 1 < len(filtered_projects):
        with col2:
            project = filtered_projects[i + 1]

            with st.container(border=True):
                if project.get("media_type") == "video":
                    st.video(project["media"], autoplay=True, muted=True, loop=True)
                else:
                    st.image(project["media"], use_container_width=True)
                st.subheader(project["title"])
                st.write(project["description"])

                st.link_button(
                    "GitHub ↗",
                    project["github"],
                    use_container_width=True
                )

st.markdown('</div>', unsafe_allow_html=True)

footer()