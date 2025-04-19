import streamlit as st
import json
from PIL import Image

st.set_page_config(page_title="RAQIB - Nuclear Inspection Assistant", layout="centered")

# عرض الشعار
logo = Image.open("raqib_logo_dark.png")
st.image(logo, width=130)

# تحميل قاعدة البيانات
with open("RAQIB_KnowledgeBase_Expanded.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# عرض اختيار اللغة من القاعدة نفسها
languages = list(knowledge.keys())
lang = st.radio("اختر اللغة | Choose Language", ["العربية", "English", "Deutsch", "한국어"])

# عرض الأقسام حسب اللغة المختارة
sections = list(knowledge[lang].keys())
selected_section = st.selectbox("اختر القسم | Select Section", sections)

# عرض المواضيع
topics = list(knowledge[lang][selected_section].keys())
selected_topic = st.selectbox("اختر الموضوع | Select Topic", topics)

# عرض المحتوى
st.markdown("### النتيجة | Result:")
st.success(knowledge[lang][selected_section][selected_topic])

# توقيع أسفل الصفحة
st.markdown("---")
col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.image("raqib_logo_dark.png", width=25)
with col2:
    st.markdown("<p style='font-size:13px; padding-top:5px;'>Nuclear Inspection Assistant</p>", unsafe_allow_html=True)
