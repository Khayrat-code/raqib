import streamlit as st
import json

# إعداد الصفحة
st.set_page_config(page_title="RAQIB - Training", layout="centered")
st.title("Awareness & Training")
st.markdown("Here you can access training materials, awareness documents, and visual guides for inspectors.")

# تحميل قاعدة البيانات
with open("RAQIB_KnowledgeBase_Expanded.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# عرض الأقسام
sections = list(knowledge.keys())
selected_section = st.selectbox("اختر القسم التدريبي | Select Training Category", sections)

# عرض المواضيع داخل القسم
if selected_section in knowledge:
    topics = list(knowledge[selected_section].keys())
    selected_topic = st.selectbox("اختر الموضوع | Select Topic", topics)
    result = knowledge[selected_section][selected_topic]

    # عرض النتيجة
    st.markdown("### المادة التدريبية | Training Content:")
    st.success(result)
else:
    st.warning("No data available for this section.")
