import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="RAQIB | Nuclear Inspection Assistant", layout="centered")

# اختيار اللغة (يظهر أعلى يمين الصفحة)
col1, col2 = st.columns([6, 2])
with col2:
    languages = {"العربية": "ar", "English": "en", "Deutsch": "de", "한국어": "kr"}
    selected = st.selectbox("اختر اللغة | Choose Language", list(languages.keys()))
    st.session_state["language"] = languages[selected]

# استخدام اللغة المختارة
lang = st.session_state["language"]

# المحتوى حسب اللغة
if lang == "ar":
    st.title("رقيب | مساعد التفتيش النووي")
    st.markdown("مرحبا بك في رقيب، المنصة الذكية لمساعدة المفتش النووي في أداء مهامه.")
    st.markdown("اختر قسمًا من القائمة الجانبية.")
elif lang == "de":
    st.title("RAQIB | Nuklearer Inspektionsassistent")
    st.markdown("Willkommen bei RAQIB, Ihrem intelligenten Assistenten für nukleare Inspektionen.")
    st.markdown("Wählen Sie einen Bereich aus der Seitenleiste.")
elif lang == "kr":
    st.title("RAQIB | 원자력 검사 도우미")
    st.markdown("RAQIB에 오신 것을 환영합니다. 왼쪽에서 섹션을 선택하세요.")
else:
    st.title("RAQIB | Nuclear Inspection Assistant")
    st.markdown("Welcome to RAQIB, your smart assistant for nuclear field inspections.")
    st.markdown("Select a section from the sidebar.")
