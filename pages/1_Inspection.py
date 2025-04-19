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

# ربط الأسماء الظاهرة بالمفاتيح الحقيقية
section_map = {
    "Nuclear Safety": "radiation_protection",
    "Regulatory Inspection": "regulatory_inspection"
}

display_sections = list(section_map.keys())
selected_display = st.selectbox("اختر القسم | Select Section", display_sections)
selected_section = section_map[selected_display]

# عرض المواضيع
topics = list(knowledge[lang][selected_section].keys())
selected_topic = st.selectbox("اختر الموضوع | Select Topic", topics)

# عرض النتيجة
st.markdown("### النتيجة | Result:")
st.success(knowledge[lang][selected_section][selected_topic])
