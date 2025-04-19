
import streamlit as st
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="RAQIB - Home", page_icon="favicon.png", layout="centered")

# الشريط الجانبي
with st.sidebar:
    logo = Image.open("favicon.png")
    st.image(logo, width=130)
    st.markdown("---")
    st.markdown("**RAQIB | رقيب**")
    st.markdown("Smart Nuclear Safety & Inspection Assistant")
    st.markdown("[@Nuclear2024](https://x.com/Nuclear2024)")

# الصفحة الرئيسية
st.markdown("<h1 style='text-align: center; color: #0a3d62;'>RAQIB | Nuclear Inspection Assistant</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

st.markdown("### Welcome to RAQIB")
st.write("This intelligent assistant helps nuclear inspectors access procedures, thresholds, and regulatory info efficiently.")
st.markdown("#### Navigate through the sections:")
st.markdown("- **Inspection Dashboard**: Review safety limits and protocols.")
st.markdown("- **Training & Awareness**: Access IAEA guides and safety manuals.")
st.markdown("- **Support & Docs**: Get technical help and regulations.")
st.success("Choose a section from the sidebar to get started.")
