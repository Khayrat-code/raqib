import streamlit as st

# التحقق من اختيار اللغة من الصفحة الرئيسية
if "language" not in st.session_state:
    st.warning("يرجى اختيار اللغة من الصفحة الرئيسية | Please select a language from the home page.")
    st.stop()

# استرجاع اللغة المختارة
lang = st.session_state.get("language", "en")

# إعداد الصفحة
st.set_page_config(page_title="RAQIB | Inspection", layout="centered")

# عرض المحتوى حسب اللغة المختارة
if lang == "ar":
    st.title("لوحة التفتيش")
    st.markdown("هذه الصفحة تتيح لك مراجعة حدود الأمان، الإجراءات، والوثائق التنظيمية.")
    st.markdown("- اختر القسم")
    st.markdown("- استعرض حدود الجرعات")
    st.markdown("- عرض بروتوكولات الفحص الميداني")

elif lang == "de":
    st.title("Inspektionsübersicht")
    st.markdown("Diese Seite bietet einen Überblick über Sicherheitsgrenzen, Protokolle und Dokumentationen.")
    st.markdown("- Kategorie auswählen")
    st.markdown("- Grenzwerte überprüfen")
    st.markdown("- Inspektionsprotokolle anzeigen")

elif lang == "kr":
    st.title("검사 대시보드")
    st.markdown("이 페이지에서는 방사선 기준, 절차, 문서를 확인할 수 있습니다.")
    st.markdown("- 범주 선택")
    st.markdown("- 기준 수치 확인")
    st.markdown("- 검사 절차 보기")

else:
    st.title("Inspection Dashboard")
    st.markdown("This page allows you to review safety limits, protocols, and documentation.")
    st.markdown("- Choose section")
    st.markdown("- Review dose thresholds")
    st.markdown("- Access field inspection protocols")
