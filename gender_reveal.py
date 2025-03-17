import streamlit as st
import time
import random
from PIL import Image, ImageDraw

# Function to create a placeholder ultrasound image
def load_ultrasound():
    try:
        return Image.open("PXL_20250227_210253940.jpg")  # Replace with the correct filename if different
    except Exception as e:
        st.error(f"Erro ao carregar a imagem: {e}")
        return None

# Set gender reveal outcome (you can replace 'boy' or 'girl' based on your NIPT result)
GENDER = random.choice(["girl"])  # Replace with actual result when available

def main():
    st.set_page_config(page_title="Baby Gender Reveal!", layout="centered")

    # Set background color based on gender
    bg_color = "#F8C8DC" if GENDER == "girl" else "#A3C1E2"
    st.markdown(
        f"""
        <style>
        body {{
            background-color: {bg_color};
        }}
        </style>
        """, unsafe_allow_html=True
    )

    # Intro section with suspense
    st.title("🎉 A Angelica tem uma surpresa para você! / Angelica has a little surprise for you! 🎉")
    time.sleep(1)
    st.write("Você sabia que a família Mattos está crescendo? / Did you know the Mattos family is growing?")

    # Slowly load the sonogram like PowerPoint effect
    st.image(load_ultrasound(), caption="Meet my little love! 💕", use_container_width=True)
    time.sleep(2)

    # Add a baby emoji text
    st.markdown("👶 Olá, eu estou com 11 semanas de vida! / Hi, I am 11 weeks old!  💕")

    # Gender guessing section
    st.write("O que você acha que sou? / What do you think?")
    guess = st.radio("Make a guess! / Faça sua aposta!", ["Boy 👦 / Menino", "Girl 👧 / Menina"], index=None)

    if guess:
        st.write("Hmmm... vamos descobrir! / Let's find out!")
        time.sleep(1)

        # Fake suspense loading
        with st.spinner("Processando coisas científicas de bebês... / Processing scientific baby vibes... 🔬🍼"):
            time.sleep(6)

        # Balloon animation
        st.write("🎈🎈🎈 POP! 🎈🎈🎈")
        time.sleep(1)

        # Drop balloons for celebration
        st.balloons()
        time.sleep(1)

        # Display gender reveal message
        st.markdown("<h1 style='text-align: center; color: #F8C8DC;'>💖 É uma MENINA! 💖<br>💖 It's a GIRL! 💖</h1>", unsafe_allow_html=True)

        # Celebration message
        st.write("Can't wait to meet my little love! 💕 / A familia mal pode esperar para conhecer meu amorzinho! 💕")

if __name__ == "__main__":
    main()
