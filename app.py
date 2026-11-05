import streamlit as st
import smtplib
import os
import time
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# --- ENTERPRISE MINIMALIST STYLING CONFIGURATION ---
st.set_page_config(page_title="MiwaExim Mail", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    /* Clean Minimalist Charcoal & Slate Theme Base */
    .stApp {
        background-color: #0F172A;
        color: #F1F5F9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Professional Sidebar Panel Setup */
    section[data-testid="stSidebar"] {
        background-color: #0B0F19 !important;
        border-right: 1px solid #334155;
    }
    
    /* 🔴 THE VISIBILITY FIX: Force ALL Sidebar and Main Panel Labels to be Bright White */
    section[data-testid="stSidebar"] label, 
    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] span,
    div[data-testid="stVerticalBlock"] label,
    .stWidgetFormLabel, 
    label {
        color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        opacity: 1 !important;
    }
    
    /* Sleek Clean Container Cards */
    div[data-testid="stVerticalBlock"] > div {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
    }
    
    /* Premium Input Fields Data Typography Settings */
    input, textarea, select {
        background-color: #0F172A !important;
        color: #FFFFFF !important; /* Text inside the input box */
        border: 1px solid #475569 !important;
        border-radius: 6px !important;
    }
    input:focus, textarea:focus {
        border-color: #38BDF8 !important;
        box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2) !important;
    }
    
    /* Enterprise Action Button (Clean Slate Gradient) */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%) !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        letter-spacing: 0.02em !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 12px 24px !important;
        transition: all 0.2s ease !important;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-1px);
        background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%) !important;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
    }
    
    /* Motivational Executive Header Banner */
    .executive-banner {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 28px;
        text-align: center;
        margin-bottom: 30px;
    }
    .gold-title {
        color: #F59E0B;
        font-size: 24px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin: 0;
    }
    .white-subtitle {
        color: #FFFFFF;
        font-size: 36px;
        font-weight: 800;
        letter-spacing: 0.02em;
        margin: 6px 0 0 0;
    }
    .sub-tagline {
        color: #94A3B8;
        font-size: 12px;
        font-weight: 500;
        letter-spacing: 0.05em;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- PREMIUM CORPORATE BRANDING HEADER ---
st.markdown("""
    <div class="executive-banner">
        <p class="gold-title">This time next year,</p>
        <p class="white-subtitle">We'll be millionaires.</p>
        <div class="sub-tagline">DREAM BIG. WORK HARD. MAKE IT HAPPEN.</div>
    </div>
""", unsafe_allow_html=True)

st.markdown('## 🏢 MiwaExim - Exporting Trust <span style="font-weight:300; font-size:20px; color:#94A3B8;"> </span>', unsafe_allow_html=True)
st.write("Import export company in Ahmedabad, Gujarat")

# --- SIDEBAR CONTROL PANEL ---
st.sidebar.markdown('### 🔐 GATEWAY CREDENTIALS')
smtp_server = st.sidebar.text_input("SMTP TARGET SERVER", value="smtp.titan.email")
port = st.sidebar.number_input("SECURE PORT", value=587)
# The script will now pull your saved credentials securely from the cloud vault
sender_email = st.sidebar.text_input("AUTHENTICATED IDENTITY (EMAIL)", value=st.secrets["GODADDY_EMAIL"])
sender_password = st.sidebar.text_input("GATEWAY PASSKEY", value=st.secrets["GODADDY_PASSWORD"], type="password")
throttle_delay = st.sidebar.slider("THROTTLE DELAY (SEC / EMAIL)", min_value=5, max_value=20, value=12)

# --- MAIN ENGINE LAYOUT ---
col1, col2 = st.columns([1.1, 0.9], gap="large")

with col1:
    st.markdown("### 📝 1. COMPOSER SUITE")
    subject = st.text_input("CAMPAIGN SUBJECT LINE", placeholder="Enter transmission subject...")
    email_mode = st.selectbox("CONTENT PROTOCOL MODE", ["Plain Text", "HTML Template"])
    body_content = st.text_area("PAYLOAD CORE BODY CONTENT", height=240, placeholder="Write text body or drop production HTML template blocks here...")

with col2:
    st.markdown("### 📂 2. DATA MATRIX & ATTACHMENTS")
    contact_file = st.file_uploader("TARGET CONTACT SOURCE (XLSX / CSV)", type=["csv", "xlsx"])
    uploaded_files = st.file_uploader("INJECT ATTACHMENT DEPLOYMENTS (MULTIPLE)", accept_multiple_files=True)
    
    st.markdown("### 🚦 3. OPERATIONAL EXECUTION")
    
    if st.button("🔥 DISPATCH CAMPAIGN STREAMED ENGINE"):
        if contact_file is not None:
            try:
                if contact_file.name.endswith('.csv'):
                    df = pd.read_csv(contact_file)
                else:
                    df = pd.read_excel(contact_file)
                    
                email_col = [col for col in df.columns if 'email' in col.lower()]
                    if email_col:
                        # We grab the first matched column name string, select the series, and extract unique values
                        matched_column = email_col[0]
                        target_list = df[matched_column].dropna().unique().tolist() #  Fixed Code

                    
                    if not sender_email or not sender_password:
                        st.error("🚨 CRITICAL OPERATION HALTED: Authentication profile data missing in terminal settings panel.")
                    else:
                        st.toast(f"MiwaExim Node Online: Loaded {len(target_list)} contacts.", icon="🔋")
                        
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
                                
                            current_prog = (index + 1) / total
                            progress_bar.progress(current_prog)
                            status_metrics.markdown(f"**🟢 Stream Status:** Delivering package `{index+1}/{total}` // Success: `{success_count}`")
                            
                            if index < total - 1:
                                time.sleep(throttle_delay)
                                
                        server.quit()
                        st.balloons()
                        st.success(f"⚡ ALL TRANSPORTS COMPLETE: Broadcast sent to {success_count}/{total} entities.")
                else:
                    st.error("🚨 SHEET SCAN REJECTED: System failed to locate an 'Email' column label.")
            except Exception as io_err:
                st.error(f"🚨 RESOURCE READ FAULT: {str(io_err)}")
        else:
            st.error("🚨 CRITICAL TARGET EXCEPTION: Drop your contact list sheet file first.")
