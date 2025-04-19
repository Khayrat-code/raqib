import streamlit as st
import json
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="RAQIB | Nuclear Inspection Assistant", layout="wide")
logo = Image.open("favicon.png")
st.image(logo, width=70)

# تحميل قاعدة البيانات الموسعة
with open("RAQIB_KnowledgeBase_Complete_Final.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# اختيار اللغة من الواجهة
selected_lang = st.selectbox("اختر اللغة | Choose Language", ["العربية", "English", "Deutsch", "한국어"])
lang = selected_lang  # لأن المفاتيح في JSON بهذا الشكل بالضبط

# نصوص واجهة المستخدم حسب اللغة
ui = {
    "العربية": {
        "title": "رقيب | المساعد الذكي للتفتيش النووي",
        "welcome": "مرحبًا بك في رقيب، اختر قسمًا للاطلاع على محتواه:",
        "topic_title": "الموضوع",
        "result": "المحتوى"
    },
    "English": {
        "title": "RAQIB | Nuclear Inspection Assistant",
        "welcome": "Welcome to RAQIB. Choose a section to explore its content:",
        "topic_title": "Topic",
        "result": "Content"
    },
    "Deutsch": {
        "title": "RAQIB | Nuklearer Inspektionsassistent",
        "welcome": "Willkommen bei RAQIB. Wählen Sie einen Bereich, um Inhalte anzuzeigen:",
        "topic_title": "Thema",
        "result": "Inhalt"
    },
    "한국어": {
        "title": "RAQIB | 원자력 검사 도우미",
        "welcome": "RAQIB에 오신 것을 환영합니다. 섹션을 선택하여 내용을 확인하세요:",
        "topic_title": "주제",
        "result": "내용"
    }
}

t = ui[lang]

# واجهة التطبيق
st.title(t["title"])
st.markdown(f"### {t['welcome']}")

# عرض جميع الأقسام داخل Expanders
for section_name, topics in knowledge[lang].items():

   import streamlit as st

# ... هنا محتوى صفحتك كامل فوق ...

# توقيع يظهر بأسفل الصفحة فقط
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
