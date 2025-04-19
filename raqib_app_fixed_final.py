import streamlit as st

st.set_page_config(
    page_title="RAQIB - رقيب",
    page_icon="favicon.png"
)

import json
import os
import re
import base64

# تحميل قاعدة البيانات من ملف JSON
with open("Expanded_IAEA_Knowledge_Base.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# واجهة المستخدم
st.title("RAQIB - Nuclear Inspection Assistant")
st.markdown("### Ask a question (English or Arabic) about nuclear safety, radiation limits, waste, or inspections.")

# إدخال المستخدم
question = st.text_input("Your question:")

# دالة للإجابة بناءً على الكلمة المفتاحية
def get_answer(q):
    q = q.lower()
    for key in knowledge:
        if key in q:
            return knowledge[key]
    return "Sorry, I could not find an answer to your question."

# عرض الإجابة
if question:
    answer = get_answer(question)
    st.markdown(f"**Answer:** {answer}")
