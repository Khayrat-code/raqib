import streamlit as st

# إعداد اللغة الافتراضية
if "language" not in st.session_state:
    st.session_state.language = "en"

# واجهة اختيار اللغة في الشريط الجانبي
lang = st.sidebar.selectbox("اختر اللغة | Choose Language", ["العربية", "English", "Deutsch", "한국어"])
if lang == "العربية":
    st.session_state.language = "ar"
elif lang == "Deutsch":
    st.session_state.language = "de"
elif lang == "한국어":
    st.session_state.language = "kr"
else:
    st.session_state.language = "en"

# قاعدة النصوص لكل لغة
texts = {
    "ar": {
        "title": "رقيب | المساعد الذكي للتفتيش النووي",
        "select_page": "اختر الصفحة",
        "home": "الرئيسية",
        "inspection": "لوحة التفتيش",
        "training": "التدريب والتوعية",
        "support": "الدعم الفني",
        "welcome": "مرحبًا بك في رقيب",
        "home_msg": "يساعدك رقيب على الوصول إلى الإجراءات والحدود التنظيمية بكل سهولة.",
        "inspection_msg": "راجع حدود الأمان والبروتوكولات حسب القسم المختار.",
        "training_msg": "استعرض أدلة الوكالة الدولية للطاقة الذرية ودروس التوعية.",
        "support_msg": "للدعم، تواصل معنا عبر: @Nuclear2024 | khayratum@gmail.com"
    },
    "en": {
        "title": "RAQIB | Nuclear Inspection Assistant",
        "select_page": "Select Page",
        "home": "Home",
        "inspection": "Inspection Dashboard",
        "training": "Training & Awareness",
        "support": "Technical Support",
        "welcome": "Welcome to RAQIB",
        "home_msg": "This intelligent assistant helps you access procedures and regulatory thresholds easily.",
        "inspection_msg": "Review safety limits and protocols by category.",
        "training_msg": "Browse IAEA guides and awareness materials.",
        "support_msg": "For support, contact us: @Nuclear2024 | khayratum@gmail.com"
    },
    "de": {
        "title": "RAQIB | Nuklearer Inspektionsassistent",
        "select_page": "Seite wählen",
        "home": "Startseite",
        "inspection": "Inspektionsübersicht",
        "training": "Schulung & Aufklärung",
        "support": "Technischer Support",
        "welcome": "Willkommen bei RAQIB",
        "home_msg": "Dieser Assistent hilft Ihnen, Richtlinien und Schwellenwerte leicht zu finden.",
        "inspection_msg": "Überprüfen Sie Sicherheitsgrenzen und Protokolle nach Kategorie.",
        "training_msg": "Durchsuchen Sie IAEA-Leitfäden und Schulungsmaterialien.",
        "support_msg": "Support: @Nuclear2024 | khayratum@gmail.com"
    },
    "kr": {
        "title": "RAQIB | 원자력 검사 도우미",
        "select_page": "페이지 선택",
        "home": "홈",
        "inspection": "검사 대시보드",
        "training": "교육 및 인식",
        "support": "기술 지원",
        "welcome": "RAQIB에 오신 것을 환영합니다",
        "home_msg": "이 도우미는 절차와 규제를 쉽게 접근할 수 있게 도와줍니다.",
        "inspection_msg": "범주별로 안전 한도 및 프로토콜을 검토하십시오.",
        "training_msg": "IAEA 가이드와 교육 자료를 살펴보세요.",
        "support_msg": "지원 문의: @Nuclear2024 | khayratum@gmail.com"
    }
}

# اللغة المختارة
t = texts[st.session_state.language]

# تحديد الصفحة من القائمة الجانبية
page = st.sidebar.radio(t["select_page"], [t["home"], t["inspection"], t["training"], t["support"]])

# عنوان رئيسي
st.title(t["title"])

# محتوى الصفحة حسب الاختيار
if page == t["home"]:
    st.subheader(t["welcome"])
    st.markdown(t["home_msg"])

elif page == t["inspection"]:
    st.subheader(t["inspection"])
    st.markdown(t["inspection_msg"])

elif page == t["training"]:
    st.subheader(t["training"])
    st.markdown(t["training_msg"])

elif page == t["support"]:
    st.subheader(t["support"])
    st.markdown(t["support_msg"])
