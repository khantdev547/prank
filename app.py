import streamlit as st
import asyncio
from telegram import Bot

# UI Styling (iOS Blur Style)
st.markdown("""
<style>
    .stApp { background-color: #F2F2F7; }
    .glass-card { background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(20px); border-radius: 20px; padding: 20px; border: 1px solid rgba(255, 255, 255, 0.3); }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.title("📱 Telegram Auto Bot")

# Input Fields
token = st.text_input("Bot API Token", type="password")
chat_id = st.text_input("Telegram User ID (Target)")
message = st.text_area("Message Content")

col1, col2 = st.columns(2)
count = col1.number_input("Count", min_value=1, value=5)
delay = col2.number_input("Delay (sec)", min_value=0.1, value=0.5)

# Async Bot Function
async def send_messages():
    bot = Bot(token=token)
    for i in range(count):
        await bot.send_message(chat_id=chat_id, text=message)
        await asyncio.sleep(delay)
    st.success("Successfully Sent!")

if st.button("🚀 START SENDING"):
    if token and chat_id and message:
        asyncio.run(send_messages())
    else:
        st.error("Please fill all fields correctly!")

st.markdown('</div>', unsafe_allow_html=True)