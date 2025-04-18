
import streamlit as st
import json

# إعداد الصفحة
st.set_page_config(page_title="رقيب RAQIB", page_icon="🛡️", layout="centered")

# تحميل قاعدة البيانات
with open("Expanded_IAEA_Knowledge_Base.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# اختيار اللغة
language = st.radio("Choose Language | اختر اللغة", ["العربية", "English"])

# ترجمة العناوين
section_titles = {
    "العربية": {
        "radiation_protection": "الحماية من الإشعاع",
        "regulatory_inspection": "التفتيش التنظيمي",
        "maintenance_and_surveillance": "الصيانة والمراقبة",
        "emergency_procedures": "إجراءات الطوارئ",
        "radiation_monitoring": "المراقبة الإشعاعية",
        "radioactive_waste_management": "إدارة النفايات المشعة",
        "transportation": "النقل",
        "nuclear_fuel_cycle": "دورة الوقود النووي",
        "nuclear_security": "الأمن النووي",
        "licensing_and_authorization": "التراخيص",
        "notable_incidents": "الحوادث النووية"
    },
    "English": {
        "radiation_protection": "Radiation Protection",
        "regulatory_inspection": "Regulatory Inspection",
        "maintenance_and_surveillance": "Maintenance and Surveillance",
        "emergency_procedures": "Emergency Procedures",
        "radiation_monitoring": "Radiation Monitoring",
        "radioactive_waste_management": "Radioactive Waste Management",
        "transportation": "Transportation",
        "nuclear_fuel_cycle": "Nuclear Fuel Cycle",
        "nuclear_security": "Nuclear Security",
        "licensing_and_authorization": "Licensing and Authorization",
        "notable_incidents": "Notable Incidents"
    }
}

# اختيار القسم
section_keys = list(knowledge.keys())
translated_sections = [section_titles[language][key] for key in section_keys]
selected_translated = st.selectbox("اختر القسم | Select Section", translated_sections)
selected_key = section_keys[translated_sections.index(selected_translated)]

# اختيار الموضوع
sub_keys = list(knowledge[selected_key].keys())
selected_sub = st.selectbox("اختر الموضوع | Select Topic", sub_keys)

# عرض الإجابة
st.markdown("### النتيجة | Result:")
response = knowledge[selected_key][selected_sub]
if isinstance(response, list):
    st.success(", ".join(response))
elif isinstance(response, dict):
    st.success("\n".join([f"{k}: {v}" for k, v in response.items()]))
else:
    st.success(response)


# توقيع أسفل الصفحة
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>برمجة: <strong>خيرات الأمير</strong></div>", unsafe_allow_html=True)
