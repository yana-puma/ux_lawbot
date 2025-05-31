
import streamlit as st
import openai
import re

# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Define UX law links
law_links = {
    "Hick’s Law": "https://lawsofux.com/hicks-law/",
    "Fitts’s Law": "https://lawsofux.com/fittss-law/",
    "Miller’s Law": "https://lawsofux.com/millers-law/",
    "Law of Proximity": "https://lawsofux.com/law-of-proximity/",
    "Law of Similarity": "https://lawsofux.com/law-of-similarity/",
    "Law of Prägnanz": "https://lawsofux.com/law-of-pragnanz/",
    "Jakob’s Law": "https://lawsofux.com/jakobs-law/",
    "Aesthetic-Usability Effect": "https://lawsofux.com/aesthetic-usability-effect/",
    "Peak-End Rule": "https://lawsofux.com/peak-end-rule/",
    "Doherty Threshold": "https://lawsofux.com/doherty-threshold/",
    "Von Restorff Effect": "https://lawsofux.com/von-restorff-effect/",
    "Tesler’s Law": "https://lawsofux.com/teslers-law/",
    "Serial Position Effect": "https://lawsofux.com/serial-position-effect/",
    "Zeigarnik Effect": "https://lawsofux.com/zeigarnik-effect/"
}

# Streamlit UI
st.set_page_config(page_title="UX LawBot", page_icon="🤖")
st.title("🤖 UX LawBot")
st.markdown("Describe your UX problem and let the chatbot suggest relevant [Laws of UX](https://lawsofux.com).")

role = st.selectbox("Your role", ["PM", "UX Designer", "Developer"])
temperature = st.slider("Temperature (controls creativity)", 0.0, 1.0, 0.5)
user_input = st.text_area("Describe a UX challenge you're facing:")

def insert_links(text):
    for law, url in law_links.items():
        pattern = re.compile(re.escape(law), re.IGNORECASE)
        text = pattern.sub(f"[{law}]({url})", text)
    return text

if st.button("Get UX Advice") and user_input:
    system_prompt = f"You are UX LawBot, an assistant that helps a {role} apply UX laws to real-world problems."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temperature,
    )
    raw_reply = response.choices[0].message.content
    st.markdown(insert_links(raw_reply))
