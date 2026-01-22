import streamlit as st
import google.generativeai as genai
import os

# 1. Configuration de l'API (Sécurisée par variable d'environnement)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Configuration du modèle (Paramètres copiés d'AI Studio)
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # Ajoutez ici vos 'System Instructions' si vous en avez
  system_instruction="Tu es un assistant expert en...", 
)

# 3. Interface utilisateur avec Streamlit
st.title("Mon Application IA")
user_input = st.text_input("Posez votre question :")

if st.button("Envoyer"):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(user_input)
    st.write(response.text)
