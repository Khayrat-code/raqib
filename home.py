import streamlit as st
import json

st.set_page_config(page_title="RAQIB | Home", page_icon="favicon.png")

# إعداد اللغة
if "language" not in st.session_state:
    st.session_state.language = "ar"

lang_options = {
    "ar": "العربية",
    "en": "English",
    "de": "Deutsch",
    "ko": "한국어"
}

lang = st.selectbox("اختر اللغة | Choose Language", options=list(lang_options.keys()),
                    format_func=lambda x: lang_options[x])
st.session_state.language = lang

# تحميل قاعدة البيانات المحدثة
with open("RAQIB_KnowledgeBase_Full_Expanded.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# ترجمات العناوين حسب اللغة
titles = {
    "ar": {
        "app_title": "رقيب | المساعد الذكي للتفتيش النووي",
        "welcome": "مرحبًا بك في رقيب، اختر قسمًا للاطلاع على محتواه:",
        "select_section": "اختر القسم",
        "select_topic": "اختر الموضوع",
        "result": "النتيجة"
    },
    "en": {
        "app_title": "RAQIB | Nuclear Inspection Assistant",
        "welcome": "Welcome to RAQIB. Choose a section to view its content:",
        "select_section": "Select Section",
        "select_topic": "Select Topic",
        "result": "Result"
    },
    "de": {
        "app_title": "RAQIB | Nuklearer Inspektionsassistent",
        "welcome": "Willkommen bei RAQIB. Wählen Sie einen Bereich aus:",
        "select_section": "Abschnitt wählen",
        "select_topic": "Thema wählen",
        "result": "Ergebnis"
    },
    "ko": {
        "app_title": "RAQIB | 원자력 검사 도우미",
        "welcome": "RAQIB에 오신 것을 환영합니다. 섹션을 선택하여 내용을 확인하세요:",
        "select_section": "섹션 선택",
        "select_topic": "주제 선택",
        "result": "결과"
    }
}

st.title(titles[lang]["app_title"])
st.write(titles[lang]["welcome"])

# عرض الأقسام والمواضيع
for section_name, topics in knowledge[lang].items():
    with st.expander(section_name):
        topic_selected = st.selectbox(titles[lang]["select_topic"], options=list(topics.keys()),
                                      key=f"{section_name}_{lang}")
        if topic_selected:
            st.markdown(f"*{titles[lang]['result']}:*")
            st.info(topics[topic_selected])

# التوقيع السفلي
st.markdown(
    """
    <div style="position: fixed; bottom: 0; width: 100%; padding: 10px 0; background-color: #f0f2f6; text-align: center; font-size: 13px; color: #555;">
        تم بواسطة خيرات الأمير
        <a href="https://twitter.com/Nuclear2024" target="_blank" style="text-decoration: none; color: #555; margin-left: 8px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/53/X_logo_2023.svg" width="14" style="vertical-align: middle; margin-right: 4px;">
            @Nuclear2024
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
