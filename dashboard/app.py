import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DATABASE_PATH

st.set_page_config(page_title="AI Cyber Threat Detection", layout="wide")

st.title("🛡️ AI-Powered Cyber Threat Simulation & Detection")
st.markdown("Real-time monitoring of Red Team attacks and Blue Team AI responses.")

def load_data():
    conn = sqlite3.connect(DATABASE_PATH)
    df = pd.read_sql_query("SELECT * FROM attacks ORDER BY id DESC", conn)
    conn.close()
    return df

# Sidebar logs
st.sidebar.header("System Logs")
if st.sidebar.button("Refresh Data"):
    st.rerun()

df = load_data()

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Attacks", len(df))
col2.metric("High Risk", len(df[df['final_risk'] == 'High']))
col3.metric("Medium Risk", len(df[df['final_risk'] == 'Medium']))
col4.metric("Low Risk", len(df[df['final_risk'] == 'Low']))

# Charts
c1, c2 = st.columns(2)

with c1:
    st.subheader("Attack Type Distribution")
    if not df.empty:
        fig_type = px.pie(df, names='attack_type', title='Attack Types')
        st.plotly_chart(fig_type, use_container_width=True)

with c2:
    st.subheader("Risk Severity Comparison")
    if not df.empty:
        # Prepare data for stacked bar or grouped bar
        risk_counts = df['final_risk'].value_counts().reset_index()
        risk_counts.columns = ['Risk Level', 'Count']
        fig_risk = px.bar(risk_counts, x='Risk Level', y='Count', color='Risk Level', 
                          color_discrete_map={'High':'red', 'Medium':'orange', 'Low':'green'})
        st.plotly_chart(fig_risk, use_container_width=True)

# Detailed Analysis View
st.subheader("🚨 Live Threat Feed")

for index, row in df.iterrows():
    with st.expander(f"[{row['final_risk']}] {row['attack_type']} - ID: {row['id']}"):
        st.code(row['content'])
        
        c1, c2, c3 = st.columns(3)
        c1.info(f"Rule Based: {row['rule_risk']}")
        c2.warning(f"OpenAI: {row['openai_risk']}")
        c3.success(f"Gemini: {row['gemini_risk']}")
        
        st.markdown(f"**AI Consolidated Reason:**\n{row['ai_reason']}")

st.markdown("---")
st.caption("Educational Purpose Only. Built with Python & Streamlit.")
