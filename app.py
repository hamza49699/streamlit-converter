import streamlit as st
from pdf2docx import Converter
import io
import time

st.set_page_config(page_title="📄 PDF to Word Converter", page_icon="🔄")

st.title("📄 Free Professional PDF to Word Converter 🔄")
st.write("📢 Easily Convert your PDF files into a fully formatted Word document with ease. 🎯")

uploaded_file = st.file_uploader("📤 Upload your PDF file", type=["pdf"])

if uploaded_file:
    try:
        if "converted_file" not in st.session_state or "last_uploaded_file" not in st.session_state or st.session_state["last_uploaded_file"] != uploaded_file.name:
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())
            
            with st.spinner("⏳ Converting your PDF to Word... Please wait. ⚡"):
                time.sleep(2) 
                
                word_io = io.BytesIO()
                cv = Converter("temp.pdf")
                cv.convert(word_io, start=0, end=None)
                cv.close()
                word_io.seek(0)
                
                st.session_state["converted_file"] = word_io 
                st.session_state["last_uploaded_file"] = uploaded_file.name  
        
        st.success("🎉✅ Conversion Successful! Download your Word file below. 📂")

        st.download_button(
            label="📥 Download Word Document",
            data=st.session_state["converted_file"].getvalue(),
            file_name="converted_document.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    
    except Exception as e:
        st.error(f"❌⚠️ Error: {str(e)}")

st.markdown("---")
st.markdown(
    "🔧 Developed by **Muhammad Hamza Javed** | 💜 Follow me on [GitHub](https://github.com/hamza49699) & [LinkedIn](https://www.linkedin.com/in/hamza-khan-7472b822b/) "
)
st.markdown("© 2025 PDF ↔ Word Converter. All rights reserved.")
