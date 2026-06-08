import streamlit as st
import time
import os

# --- iOS Modern Design CSS ---
st.markdown("""
<style>
    .stApp { background-color: #F2F2F7; }
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
    }
    div.stButton > button {
        border-radius: 12px;
        border: none;
        background-color: #007AFF;
        color: white;
        width: 100%;
        padding: 12px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# --- UI Interface ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.title("📱 Telegram Auto")
message = st.text_area("Message Content")

col1, col2 = st.columns(2)
count = col1.number_input("Count", min_value=1, value=5)
start_sleep = col2.number_input("Start Delay (sec)", min_value=1, value=5)
delay = st.number_input("Delay between (sec)", min_value=0.1, value=0.5)

if 'running' not in st.session_state:
    st.session_state.running = False

# --- Automation Logic ---
def run_automation():
    st.session_state.running = True
    # Initial countdown
    progress = st.progress(0)
    for i in range(start_sleep):
        if not st.session_state.running: break
        time.sleep(1)
        progress.progress((i+1)/start_sleep)
    
    # Message Loop
    if st.session_state.running:
        for i in range(count):
            if not st.session_state.running: break
            # Mac AppleScript Command
            os.system(f'osascript -e \'tell application "System Events" to keystroke "{message}"\'')
            os.system('osascript -e \'tell application "System Events" to key code 36\'')
            time.sleep(delay)
        st.session_state.running = False
        st.rerun()

# Button Switch
if st.session_state.running:
    if st.button("⏹ STOP"):
        st.session_state.running = False
        st.rerun()
else:
    if st.button("▶ START"):
        run_automation()

st.markdown('</div>', unsafe_allow_html=True)