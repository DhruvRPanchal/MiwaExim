import streamlit as st
import smtplib
import os
import time
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# --- ULTRA PREMIUM MATRIX STYLING (Injected CSS) ---
st.set_page_config(page_title="CYBERMAIL // Core Engine", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    /* Premium Obsidian & Cyberpunk Glow Theme */
    .stApp {
        background-color: #0B0F19;
        color: #E2E8F0;
        font-family: 'Inter', system-ui, sans-serif;
    }
    
    /* Sleek Sidebar Customization */
    section[data-testid="stSidebar"] {
        background-color: #070A12 !important;
        border-right: 1px solid #1E293B;
    }
    
    /* Glassmorphism Premium Container Cards */
    div[data-testid="stVerticalBlock"] > div {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid #1E293B;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.4);
    }
    
    /* Custom Input Fields Customization */
    input, textarea, select {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
        border: 1px solid #334155 !important;
        border-radius: 6px !important;
    }
    input:focus, textarea:focus {
        border-color: #00F2FE !important;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.2) !important;
    }
    
    /* High-End Badass Action Buttons */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #00F2FE 0%, #4FACFE 100%) !important;
        color: #070A12 !important;
        font-weight: 700 !important;
        letter-spacing: 0.05em !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 14px 28px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.4);
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.7);
    }
    
    /* Dynamic Headers */
    h1, h2, h3 {
        color: #F8FAFC;
        font-weight: 800;
        letter-spacing: -0.02em;
    }
    .cyan-glow {
        color: #00F2FE;
        text-shadow: 0 0 8px rgba(0, 242, 254, 0.5);
    }
    </style>
""", unsafe-allow_index=True)

# --- APP LAYOUT STRUCTURE ---
st.markdown('# ⚡ <span class="cyan-glow">CYBERMAIL</span> // <span style="font-weight:300; font-size:24px;">PREMIUM CAMPAIGN MATRIX</span>', unsafe-allow_index=True)
st.write("Lightweight, zero-bloat standalone bulk delivery node configured for Titan Gateways.")

# --- SIDEBAR: SECURE TERMINAL SETTINGS ---
st.sidebar.markdown('### 🔐 GATEWAY CREDENTIALS')
smtp_server = st.sidebar.text_input("SMTP TARGET SERVER", value="smtp.titan.email")
port = st.sidebar.number_input("SECURE PORT", value=587)
sender_email = st.sidebar.text_input("AUTHENTICATED IDENTITY (EMAIL)", placeholder="sender@domain.com")
sender_password = st.sidebar.text_input("GATEWAY PASSKEY", type="password")

st.sidebar.markdown('---')
st.sidebar.markdown('### ⚙️ SAFETY SYSTEM ENGINE')
throttle_delay = st.sidebar.slider("THROTTLE DELAY (SEC / EMAIL)", min_value=5, max_value=20, value=12,
                                   help="Crucial safety windows for Titan limits. 12s keeps delivery optimized.")

# --- MAIN INTERFACE: ROW COGNITIVE SPLIT ---
col1, col2 = st.columns([1.1, 0.9], gap="large")

with col1:
    st.markdown("### 📝 1. COMPOSER SUITE")
    subject = st.text_input("CAMPAIGN SUBJECT LINE", placeholder="Enter premium transmission subject...")
    email_mode = st.segmented_control("CONTENT PROTOCOL", ["Plain Text", "HTML Template"], default="Plain Text")
    body_content = st.text_area("PAYLOAD CORE BODY CONTENT", height=240, placeholder="Write payload text or drop advanced production HTML structures here...")

with col2:
    st.markdown("### 📂 2. DATA MATRIX & ATTACHMENTS")
    contact_file = st.file_uploader("TARGET CONTACT SOURCE (XLSX / CSV)", type=["csv", "xlsx"])
    uploaded_files = st.file_uploader("INJECT ATTACHMENT DEPLOYMENTS (MULTIPLE)", accept_multiple_files=True)
    
    st.markdown("### 🚦 3. OPERATIONAL EXECUTION")
    
    # Broadcast processing loop framework logic
    if st.button("🔥 DISPATCH CAMPAIGN STREAMED ENGINE"):
        if contact_file is not None:
            try:
                # High-speed data extraction logic
                if contact_file.name.endswith('.csv'):
                    df = pd.read_csv(contact_file)
                else:
                    df = pd.read_excel(contact_file)
                    
                email_col = [col for col in df.columns if 'email' in col.lower()]
                if email_col:
                    target_list = df[email_col].dropna().unique().tolist()
                    
                    if not sender_email or not sender_password:
                        st.error("🚨 CRITICAL OPERATION HALTED: Authentication profile data missing in terminal settings panel.")
                    else:
                        st.toast(f"Matrix Node Online: Synchronized {len(target_list)} unique targets.", icon="🔋")
                        
                        # --- CONCURRENT LIVE DELIVERY ENGINE REPORT ---
                        progress_bar = st.progress(0)
                        status_metrics = st.empty()
                        
                        total = len(target_list)
                        success_count = 0
                        
                        server = smtplib.SMTP(smtp_server, port)
                        server.starttls()
                        server.login(sender_email, sender_password)
                        
                        for index, email in enumerate(target_list):
                            try:
                                msg = MIMEMultipart()
                                msg['From'] = sender_email
                                msg['To'] = email
                                msg['Subject'] = subject
                                
                                mime_fmt = 'html' if email_mode == "HTML Template" else 'plain'
                                msg.attach(MIMEText(body_content, mime_fmt))
                                
                                for f in uploaded_files:
                                    part = MIMEBase('application', "octet-stream")
                                    part.set_payload(f.getvalue())
                                    encoders.encode_base64(part)
                                    part.add_header('Content-Disposition', f'attachment; filename="{f.name}"')
                                    msg.attach(part)
                                
                                server.sendmail(sender_email, email, msg.as_string())
                                success_count += 1
                            except Exception as fail_trace:
                                st.sidebar.error(f"Drop target failure [{email}]: {str(fail_trace)}")
                                
                            # Streamed UI data updates
                            current_prog = (index + 1) / total
                            progress_bar.progress(current_prog)
                            status_metrics.markdown(f"**🟢 Stream Status:** Delivering package `{index+1}/{total}` // Node Success Score: `{success_count}`")
                            
                            if index < total - 1:
                                time.sleep(throttle_delay)
                                
                        server.quit()
                        st.balloons()
                        st.success(f"⚡ ALL TRANSPORTS COMPLETE: Successfully broadcasted to {success_count}/{total} entities.")
                else:
                    st.error("🚨 SHEET SCAN REJECTED: System mapping failed to detect any valid columns labeled 'Email'.")
            except Exception as io_err:
                st.error(f"🚨 RESOURCE READ FAULT: {str(io_err)}")
        else:
            st.error("🚨 CRITICAL TARGET FRAME EXCEPTION: Please drop your target dataset matrix sheet to configure pipeline variables.")
