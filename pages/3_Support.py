
import streamlit as st
from PIL import Image
import json

st.set_page_config(page_title="RAQIB - Support", page_icon="favicon.png", layout="centered")

with st.sidebar:
    logo = Image.open("favicon.png")
    st.image(logo, width=130)
    st.markdown("---")
    st.markdown("**RAQIB | رقيب**")
    st.markdown("Smart Nuclear Safety & Inspection Assistant")
    st.markdown("[@Nuclear2024](https://x.com/Nuclear2024)")

st.markdown("<h1 style='text-align: center; color: #0a3d62;'>RAQIB Support</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

with open("RAQIB_KnowledgeBase_Expanded.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

sections = list(knowledge.keys())
selected_section = st.selectbox("اختر نوع الدعم | Select Support Category", sections)

if selected_section in knowledge:
    topics = list(knowledge[selected_section].keys())
    selected_topic = st.selectbox("اختر عنصر الدعم | Select Support Topic", topics)
    result = knowledge[selected_section][selected_topic]
    st.markdown("### الدعم الفني | Technical Support:")
    st.success(result)
else:
    st.warning("No data available for this section.")
