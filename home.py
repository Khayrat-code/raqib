import streamlit as st
import json
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="RAQIB | Nuclear Inspection Assistant", layout="wide")
logo = Image.open("favicon.png")
st.image(logo, width=70)

# تحميل قاعدة المعرفة
with open("RAQIB_KnowledgeBase_Multilang_Complete.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# اللغة الافتراضية
if "language" not in st.session_state:
    st.session_state.language = "English"

# اختيار اللغة من الواجهة
lang_options = {
    "العربية": "Arabic",
    "English": "English",
    "Deutsch": "German",
    "한국어": "Korean"
}
selected_lang_display = st.selectbox("اختر اللغة | Choose Language", list(lang_options.keys()))
st.session_state.language = lang_options[selected_lang_display]
lang = st.session_state.language

# نصوص واجهة المستخدم حسب اللغة
ui = {
    "Arabic": {
        "title": "رقيب | المساعد الذكي للتفتيش النووي",
        "welcome": "مرحبًا بك في رقيب، اختر قسمًا للاطلاع على محتواه:",
        "section_title": "القسم",
        "topic_title": "الموضوع",
        "result": "المحتوى"
    },
    "English": {
        "title": "RAQIB | Nuclear Inspection Assistant",
        "welcome": "Welcome to RAQIB. Choose a section to explore its content:",
        "section_title": "Section",
        "topic_title": "Topic",
        "result": "Content"
    },
    "German": {
        "title": "RAQIB | Nuklearer Inspektionsassistent",
        "welcome": "Willkommen bei RAQIB. Wählen Sie einen Bereich, um Inhalte anzuzeigen:",
        "section_title": "Abschnitt",
        "topic_title": "Thema",
        "result": "Inhalt"
    },
    "Korean": {
        "title": "RAQIB | 원자력 검사 도우미",
        "welcome": "RAQIB에 오신 것을 환영합니다. 섹션을 선택하여 내용을 확인하세요:",
        "section_title": "섹션",
        "topic_title": "주제",
        "result": "내용"
    }
}

t = ui[lang]

st.title(t["title"])
st.markdown(f"### {t['welcome']}")

# عرض كل الأقسام ومحتواها داخل الصفحة
for section_name, topics in knowledge[lang].items():
    with st.expander(f"📂 {section_name}", expanded=False):
        topic_selected = st.selectbox(labels["select_topic"], topics)
