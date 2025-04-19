import streamlit as st
import json

# تحميل قاعدة البيانات
with open("RAQIB_KnowledgeBase_Expanded.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# تعريف عنوان الصفحة
st.set_page_config(page_title="RAQIB - Inspection")

# واجهة المستخدم
st.title("Inspection Dashboard")
st.markdown("Use this interface to access inspection-related guidance, safety thresholds, and categorized topics.")

# اختيار اللغة
languages = list(knowledge.keys())
lang = st.radio("اختر اللغة | Choose Language", languages)

# تعريف خريطة الأقسام
section_map = {
    "Nuclear_Safety": "radiation_protection",
    "Radiation_Monitoring": "regulatory_inspection",
    "Nuclear_Waste": "waste_limits",
    "Inspections_Regulations": "regulatory_inspection",
    "Fuel_Cycle": "fuel_data",
    "signature": "regulatory_signature"  # مؤقت لاستخدام توقيع أو دليل
}

# اختيار القسم
section_names = list(section_map.keys())
selected_section = st.selectbox("اختر القسم | Select Section", section_names)

# التحقق من وجود اللغة والقسم داخل قاعدة البيانات
try:
    actual_section = section_map[selected_section]
    section_data = knowledge.get(lang, {}).get(actual_section)

    if section_data is None:
        st.warning("No data available for this section in the selected language.")
    else:
        topics = list(section_data.keys())
        selected_topic = st.selectbox("اختر الموضوع | Select Topic", topics)

        result = section_data.get(selected_topic)
        st.markdown("### النتيجة | Result:")
        st.success(result)

except Exception as e:
    st.error(f"حدث خطأ أثناء تحميل البيانات: {e}")
