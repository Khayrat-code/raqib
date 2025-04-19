import streamlit as st
import json

# إعداد الصفحة
st.set_page_config(page_title="RAQIB - Inspection", layout="centered")
st.title("Inspection Dashboard")
st.markdown("Use this interface to access inspection-related guidance, safety thresholds, and categorized topics.")

# تحميل قاعدة البيانات
with open("RAQIB_KnowledgeBase_Expanded.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# عرض الأقسام المتوفرة
sections = list(knowledge.keys())
selected_section = st.selectbox("اختر القسم | Select Section", sections)

# عرض المواضيع داخل القسم المحدد
if selected_section in knowledge:
    topics = list(knowledge[selected_section].keys())
    selected_topic = st.selectbox("اختر الموضوع | Select Topic", topics)
    result = knowledge[selected_section][selected_topic]

    # عرض النتيجة
    st.markdown("### النتيجة | Result:")
    st.success(result)
else:
    st.warning("No data available for this section.")
