import streamlit as st


def footer():
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">

    <div style="text-align: center; padding: 50px 0 20px 0; margin-top: 80px; border-top: 1px solid #ddd; color: #777;">
        <div style="font-size: 18px; font-weight: 600; color: #444; margin-bottom: 5px;">
            Ingunn Tonetta Erdal
        </div>
        <div style="font-size: 14px; margin-bottom: 20px;">
            Digital Infrastructure and Cybersecurity student @ NTNU
        </div>
        <div style="display: flex; justify-content: center; gap: 22px; margin-bottom: 20px;">
            <a href="https://mail.google.com/mail/?view=cm&fs=1&to=erdalingunn@gmail.com" target="_blank" style="color: #EA4335; font-size: 24px; text-decoration: none;">
                <i class="fa-brands fa-google"></i>
            </a>
            <a href="https://www.linkedin.com/in/ingunn-tonetta-erdal/" target="_blank" style="color: #0077B5; font-size: 24px; text-decoration: none;">
                <i class="fa-brands fa-linkedin"></i>
            </a>
            <a href="https://github.com/ingunntonetta/" target="_blank" style="color: #333333; font-size: 24px; text-decoration: none;">
                <i class="fa-brands fa-github"></i>
            </a>
        </div>
        <div style="font-size: 12px; margin-top: 25px; color: #999;">
            © 2026 Ingunn Tonetta Erdal
        </div>
    </div>
    """, unsafe_allow_html=True)

