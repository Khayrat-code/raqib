import streamlit as st
import json

st.set_page_config(page_title="RAQIB - Inspection")

st.title("Inspection Dashboard")

# تحميل قاعدة البيانات
with open("RAQIB_KnowledgeBase_Multilang.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# اختيار اللغة
languages = list(knowledge.keys())
lang = st.radio("اختر اللغة | Choose Language", languages)

# الأقسام المخصصة للعرض، وربطها بالمسميات في JSON
section_map = {
    "Nuclear_Safety": "radiation_protection",
    "Dose_Limits": "collective_dose_limit",
    "Inspection_Rules": "regulatory_inspection"
}

display_sections = list(section_map.keys())
selected_display = st.selectbox("اختر القسم | Select Section", display_sections)
selected_section = section_map[selected_display]

# المواضيع
topics = list(knowledge[lang][selected_section].keys())
selected_topic = st.selectbox("اختر الموضوع | Select Topic", topics)

# عرض النتيجة
st.markdown("### النتيجة | Result:")
st.success(knowledge[lang][selected_section][selected_topic])
