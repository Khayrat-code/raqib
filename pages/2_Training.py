import streamlit as st
import json

# إعداد الصفحة
st.set_page_config(page_title="RAQIB - Training", layout="centered")
st.title("Awareness & Training")

# تحميل قاعدة المعرفة
with open("RAQIB_KnowledgeBase_Expanded.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# اختيار اللغة
languages = list(knowledge.keys())
lang = st.radio("اختر اللغة | Choose Language", languages)

# اختيار القسم
sections = list(knowledge[lang].keys())
selected_section = st.selectbox("اختر القسم التدريبي | Select Training Category", sections)

# اختيار الموضوع
topics = list(knowledge[lang][selected_section].keys())
selected_topic = st.selectbox("اختر المادة التدريبية | Select Training Topic", topics)

# عرض النتيجة
st.markdown("### المحتوى | Content:")
st.success(knowledge[lang][selected_section][selected_topic])
