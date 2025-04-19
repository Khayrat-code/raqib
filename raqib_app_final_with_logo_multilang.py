import streamlit as st
import json
from PIL import Image

st.set_page_config(page_title="RAQIB - Nuclear Inspection Assistant", layout="centered")

# عرض الشعار في الأعلى
logo = Image.open("favicon.png")
st.image(logo, width=130)

# اختيار اللغة
st.markdown("### اختر اللغة | Choose Language")
lang = st.radio("", ["العربية", "English"])

# تحميل قاعدة البيانات
with open("RAQIB_KnowledgeBase_Expanded.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# الأقسام والمواضيع
sections = {
    "العربية": {
        "الحماية من الإشعاع": {
            "الحد المهني": "occupational_exposure_limit",
            "حد العامة": "public_exposure_limit"
        },
        "النفايات المشعة": {
            "تصنيف النفايات": "waste_classification",
            "متطلبات التخزين": "waste_storage"
        }
    },
    "English": {
        "Radiation Protection": {
            "Occupational Limit": "occupational_exposure_limit",
            "Public Limit": "public_exposure_limit"
        },
        "Radioactive Waste": {
            "Waste Classification": "waste_classification",
            "Storage Requirements": "waste_storage"
        }
    }
}

# عرض خيارات الأقسام
st.markdown("### اختر القسم | Select Section")
selected_section = st.selectbox("", list(sections[lang].keys()))

# عرض المواضيع
st.markdown("### اختر الموضوع | Select Topic")
topics = sections[lang][selected_section]
selected_topic_label = st.selectbox("", list(topics.keys()))
selected_topic_key = topics[selected_topic_label]

# عرض النتيجة
st.markdown("### النتيجة | Result:")
st.success(knowledge[selected_topic_key])

# التوقيع أسفل الصفحة
st.markdown("---")
col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.image("raqib_logo_dark.png", width=25)
with col2:
    st.markdown("<p style='font-size:13px; padding-top:5px;'>Nuclear Inspection Assistant</p>", unsafe_allow_html=True)
