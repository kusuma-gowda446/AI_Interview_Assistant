import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI Interview Assistant',layout='centered')
st.title('AI Interview Assistant')
st.caption('practice interviews with AI ')
st.caption('Lunched by : Kusuma Gowda ')
st.write("Department of AI & DS")

try:
  client = Groq(api_key=st.secrets["GROQ_API_KEY"])
  st.write("API connection sucessful")
except(Keyerror , Filenotfounderror):
  st.error("GROQ_API_KEY is missing ")
  st.stop()

role = st.selectbox(
    "Select Job Role:",
    [
        "Python Developer",
        "Java Developer",
        "Data Analyst",
        "Machine Learning",
        "Software Engineer",
        "HR Executive"
    ]
)


if st.button("Generate Interview Questions"):
  prompt = "Generate 5 interview questions for the role of " + role

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are an expert technical interviewer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    output = response.choices[0].message.content

    st.write(output)

