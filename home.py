import streamlit as st

# إعداد الصفحة
st.set_page_config(
    page_title="RAQIB | Nuclear Inspection Assistant",
    layout="wide",
    page_icon="favicon.png"
)

# تخزين اللغة في الجلسة
if "language" not in st.session_state:
    st.session_state.language = "English"

# لغة المستخدم (تظهر في أعلى اليمين)
with st.container():
    col1, col2 = st.columns([8, 1])
    with col2:
        st.session_state.language = st.radio(
            "", ["العربية", "English", "Deutsch", "한국어"], index=["العربية", "English", "Deutsch", "한국어"].index(st.session_state.language),
            horizontal=False, label_visibility="collapsed"
        )

# ترجمة حسب اللغة
lang = st.session_state.language

if lang == "العربية":
    st.title("رقيب | مساعد التفتيش النووي")
    st.markdown("---")
    st.markdown("مرحبًا بك في رقيب، مساعد ذكي يساعد المفتشين النوويين في الوصول إلى الإجراءات والحدود والمعلومات التنظيمية.")
    st.markdown("### تصفح الأقسام:")
    st.markdown("- *لوحة التفتيش:* مراجعة حدود السلامة والبروتوكولات.")
    st.markdown("- *التدريب والتوعية:* الوصول إلى أدلة الوكالة الدولية للطاقة الذرية وكتيبات السلامة.")
    st.markdown("- *الدعم الفني:* المساعدة التقنية والمستندات التنظيمية.")
    st.success("اختر قسمًا من الشريط الجانبي للبدء.")

elif lang == "Deutsch":
    st.title("RAQIB | Nuklearer Inspektionsassistent")
    st.markdown("---")
    st.markdown("Willkommen bei RAQIB, einem intelligenten Assistenten für Inspektoren im nuklearen Bereich.")
    st.markdown("### Abschnitte:")
    st.markdown("- *Inspektions-Dashboard:* Sicherheitsgrenzwerte und Protokolle.")
    st.markdown("- *Training & Bewusstsein:* IAEA-Leitfäden und Sicherheitsdokumente.")
    st.markdown("- *Support & Dokumentation:* Technische Hilfe und Vorschriften.")
    st.success("Wählen Sie einen Abschnitt aus der Seitenleiste aus.")

elif lang == "한국어":
    st.title("RAQIB | 원자력 검사 도우미")
    st.markdown("---")
    st.markdown("RAQIB에 오신 것을 환영합니다. 이 도우미는 검사관이 절차, 기준, 규제를 빠르게 찾을 수 있게 도와줍니다.")
    st.markdown("### 섹션 탐색:")
    st.markdown("- *검사 대시보드:* 안전 기준 및 프로토콜.")
    st.markdown("- *교육 및 인식:* IAEA 가이드 및 매뉴얼.")
    st.markdown("- *지원 및 문서:* 기술 지원 및 규제 정보.")
    st.success("왼쪽 사이드바에서 섹션을 선택하세요.")

else:
    st.title("RAQIB | Nuclear Inspection Assistant")
    st.markdown("---")
    st.markdown("Welcome to RAQIB, the intelligent assistant for nuclear inspectors.")
    st.markdown("### Navigate through the sections:")
    st.markdown("- *Inspection Dashboard:* Review safety limits and protocols.")
    st.markdown("- *Training & Awareness:* Access IAEA guides and safety manuals.")
    st.markdown("- *Support & Docs:* Get technical help and regulations.")
    st.success("Choose a section from the sidebar to get started.")
