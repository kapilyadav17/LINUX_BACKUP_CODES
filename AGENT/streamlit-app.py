import streamlit as st
import pandas as pd

st.set_page_config(page_title="📊 Data Analyst Agent", layout="wide")
st.title("📊 Data Analyst Agent (LLaMA-4 Maverick)")

# File upload
uploaded_file = st.file_uploader("📁 Upload your data/document file", type=["csv", "xlsx", "txt", "pdf", "docx", "png", "jpg", "jpeg"])

if uploaded_file:
    # Use your custom backend function to parse the file
    df, ftype = parse_file(uploaded_file)
    st.success(f"✅ Loaded {ftype.upper()} file")
    st.dataframe(df)

    # Text input
    question = st.text_input("💬 Ask a question about the data")

    # Analyze button
    if st.button("🔍 Analyze"):
        if not question.strip():
            st.warning("❗ Please enter a question.")
        else:
            with st.spinner("🧠 Thinking..."):
                prompt = build_prompt(df, question)     # <- your function
                response = ask_llama(prompt)            # <- your function
            st.markdown("### 🤖 Response:")
            st.code(response)
