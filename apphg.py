import streamlit as st
import cohere

# --- SETUP ---
st.set_page_config(page_title="Landing Page Copy Optimizer", page_icon="📝")
st.title("📝 Landing Page Copy Optimizer GPT")
st.caption("Paste your landing page content and get AI-powered optimized copy using Cohere!")

# --- INIT COHERE ---
co = cohere.Client(st.secrets["COHERE_API_KEY"])

# --- UI Elements ---
lp_text = st.text_area("Paste your current landing page copy:", height=200)

tone = st.selectbox("Choose tone/style:", ["Professional", "Friendly", "Persuasive", "Minimalist", "SEO-focused"])

optimize_goal = st.radio("Optimize for:", ["More conversions", "Better clarity", "User trust", "SEO ranking"])

submit = st.button("✨ Optimize Now")

# --- Generate Response ---
if submit and lp_text:
    with st.spinner("Optimizing your copy..."):

        prompt = f"""
You are an expert in UX writing and AI content strategy.

Rewrite the following landing page copy to be optimized for: {optimize_goal}.
Use a {tone.lower()} tone.
Keep it short, impactful, and conversion-optimized.

Landing Page Copy:
\"\"\"{lp_text}\"\"\"
"""

        try:
            response = co.generate(
                model="command-light",
                prompt=prompt,
                max_tokens=300,
                temperature=0.7,
            )

            optimized_text = response.generations[0].text.strip()
            st.subheader("🚀 Optimized Landing Page Copy")
            st.success(optimized_text)

        except Exception as e:
            st.error(f"❌ Error: {e}")
