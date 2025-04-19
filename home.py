import streamlit as st

st.set_page_config(page_title="RAQIB - Home", layout="centered")

# Logo and Title
st.image("raqib_logo_temp.png", width=120)
st.title("Welcome to RAQIB")

# Description
st.markdown("""
**RAQIB** is a smart digital assistant designed to support nuclear inspectors with multilingual, real-time access to safety standards, inspection protocols, and waste classification guidance.

Built to align with IAEA regulations, RAQIB enhances field efficiency, reduces human error, and transforms inspection into a modern, data-driven process.
""")

# Navigation Buttons
st.markdown("### Navigate to:")
col1, col2, col3 = st.columns(3)
with col1:
    st.page_link("pages/1_Inspection.py", label="Inspection", icon="🧪")
with col2:
    st.page_link("pages/2_Training.py", label="Awareness", icon="📘")
with col3:
    st.page_link("pages/3_Support.py", label="Support", icon="🛠️")

# Footer
footer = """
<div style='text-align:center; font-size:13px; color:gray;'>
    Designed & Developed by Khayrat Alameer<br>
    <a href="mailto:khayratum@gmail.com">khayratum@gmail.com</a> |
    <a href="https://twitter.com/Nuclear2024" target="_blank">@Nuclear2024</a>
</div>
"""
st.markdown("---")
st.markdown(footer, unsafe_allow_html=True)