mport streamlit as st
import json

# تحميل قاعدة البيانات
with open("RAQIB_KnowledgeBase_Expanded.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# إعداد الصفحة
st.set_page_config(page_title="RAQIB - Inspection")
st.title("Inspection Dashboard")
st.markdown("Use this interface to access inspection-related guidance, safety thresholds, and categorized topics.")

# اختيار اللغة
languages = list(knowledge.keys())
lang = st.radio("اختر اللغة | Choose Language", languages)

# الأقسام المرتبطة بالتفتيش
inspection_sections = {
    "Nuclear_Safety": "radiation_protection",
    "Radiation_Monitoring": "regulatory_inspection",
    "Nuclear_Waste": "waste_limits",
    "Inspections_Regulations": "regulatory_inspection",
    "Fuel_Cycle": "fuel_data",
    "signature": "regulatory_signature"
}

selected_label = st.selectbox("اختر القسم | Select Section", list(inspection_sections.keys()))
actual_key = inspection_sections[selected_label]

# التحقق من وجود اللغة والقسم في قاعدة البيانات
if lang in knowledge:
    if actual_key in knowledge[lang]:
        topics = list(knowledge[lang][actual_key].keys())
        selected_topic = st.selectbox("اختر الموضوع | Select Topic", topics)
        result = knowledge[lang][actual_key].get(selected_topic, "لا توجد بيانات لهذا الموضوع.")
        st.markdown("### النتيجة | Result:")
        st.success(result)
    else:
        st.warning("No data available for this section in the selected language.")
else:
    st.error("اللغة غير موجودة في قاعدة البيانات.")
