import streamlit as st
import streamlit as st
import cohere

cohere_api_key = st.secrets["COHERE_API_KEY"]
co = cohere.Client(cohere_api_key)


# --- Page config ---
st.set_page_config(page_title="Landing Page Copy Optimizer GPT", page_icon="📝")
st.title("📝 Landing Page Copy Optimizer GPT (Cohere)")
st.write("Paste your landing page content and get AI-powered optimized copy using Cohere!")

# --- API Key ---
api_key = st.secrets["COHERE_API_KEY"] if "COHERE_API_KEY" in st.secrets else st.text_input("Enter your Cohere API key", type="password")

# --- Inputs ---
lp_text = st.text_area("📋 Paste your current landing page copy:", height=200)
tone = st.selectbox("🎯 Choose tone/style:", ["Professional", "Friendly", "Persuasive", "Minimalist", "SEO-focused"])
optimize_goal = st.radio("💡 Optimize for:", ["More conversions", "Better clarity", "User trust", "SEO ranking"])
submit = st.button("✨ Optimize Now")

# --- Cohere Processing ---
if submit and lp_text and api_key:
    co = cohere.Client(api_key)
    with st.spinner("Generating optimized copy..."):
        prompt = f"""
You are a professional AI content strategist and UX copywriting expert.

Your task is to rewrite the following landing page copy to improve: {optimize_goal}.
Use a {tone.lower()} tone.
Keep it concise: limit to 3–4 impactful sentences max.
Ensure it's clear, persuasive, and easy to understand.

Landing Page Copy:
\"\"\"{lp_text}\"\"\"
"""


        try:
            response = co.generate(
                model="command-r-plus",
                prompt=prompt,
                max_tokens=150,
                temperature=0.7
            )
            optimized_text = response.generations[0].text.strip()
            st.subheader("🚀 Optimized Landing Page Copy")
            st.success(optimized_text)

        except Exception as e:
            st.error(f"❌ Error: {e}")
