import streamlit as st
import json

# إعداد صفحة Streamlit
st.set_page_config(page_title="RAQIB | Home", layout="wide", page_icon="favicon.png")

# تحميل قاعدة المعرفة الموسعة متعددة اللغات
with open("RAQIB_KnowledgeBase_Full_Expanded.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# قائمة اللغات المتاحة
languages = {
    "العربية": "ar",
    "English": "en",
    "Deutsch": "de",
    "한국어": "ko"
}

# اختيار اللغة في أعلى الصفحة
selected_lang_label = st.selectbox("اختر اللغة | Choose Language", list(languages.keys()))
lang = languages[selected_lang_label]

# حفظ اللغة المختارة في session_state
st.session_state["language"] = lang

# ترجمة عنوان الصفحة حسب اللغة
titles = {
    "ar": "رقيب | المساعد الذكي للتفتيش النووي",
    "en": "RAQIB | Nuclear Inspection Assistant",
    "de": "RAQIB | Nuklearer Inspektionsassistent",
    "ko": "RAQIB | 원자력 검사 도우미"
}

subtitles = {
    "ar": "مرحباً بك في رقيب. اختر قسماً للاطلاع على محتواه:",
    "en": "Welcome to RAQIB. Choose a section to view its content:",
    "de": "Willkommen bei RAQIB. Wählen Sie einen Bereich aus, um den Inhalt anzuzeigen:",
    "ko": "RAQIB에 오신 것을 환영합니다. 내용을 보려면 섹션을 선택하세요:"
}

st.markdown(f"### {titles[lang]}")
st.markdown(subtitles[lang])

# عرض محتوى الأقسام حسب اللغة
if lang in knowledge:
    for section_name, topics in knowledge[lang].items():
        with st.expander(section_name):
            for topic, value in topics.items():
                st.markdown(f"*{topic}*")
                st.info(value)
else:
    st.warning("لا توجد بيانات لهذه اللغة. | No data found for this language.")

# توقيع في أسفل الصفحة
st.markdown("---")
st.markdown('<div style="text-align: center; font-size: 14px;">تم بواسطة خيرات الأمير | <a href="https://twitter.com/Nuclear2024" target="_blank">@Nuclear2024</a></div>', unsafe_allow_html=True)
