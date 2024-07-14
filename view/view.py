import streamlit as st
import json
import pandas as pd
from handler.pentest import run_pentest
from handler.rulebased import rulebased
from handler.indekskor import indekskor
from handler.owasp10 import owasp10
from handler.dashboard import dashboard
from datetime import datetime, timedelta

def render_app():
    st.markdown(
        """
        <style>
        .container {
            padding: 2rem;
        }
        .btn {
            margin-top: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Sistem Pakar Prediksi Serangan pada Website")

    url = st.text_input("Masukkan URL yang akan di-scan:", "http://test.com")

    if st.button("Submit"):
        st.write(f'Starting penetration test for target: {url}')
        start = datetime.now()

        # FOR REAL SCANNING USE THIS CODE (MUST INSTALL ZAP)
        # ---------------------------
        # progress_text = st.empty()
        # def update_progress(progress_message):
        #     progress_text.text(progress_message)
        # data = run_pentest(url, update_progress)
        # ----------------------------
        
        # FOR TEST SCANNING USE THIS CODE
        # ----------------------------
        with open('./sample.json', 'r') as file:
            raw = json.load(file)
            data = [item for item in raw if item['confidence'] in ['Medium', 'High'] and item['risk'] != 'Informational']
        # ----------------------------
        
        st.write('Penetration test has completed!')
        end = datetime.now()
        st.header('Scan Summary', divider='rainbow')
        scanSum(url,start,end)
        dashboard(data)
        details(data)

def scanSum(url,start,end):
    scan_duration = end - start
    formatted_duration = str(timedelta(seconds=scan_duration.seconds))
    data = {
        'URL': [url],
        'Start Time': [start],
        'End Time': [end],
        'Scan Duration': [formatted_duration],
        'Status': ['Finished']
    }

    df = pd.DataFrame(data)
    table_html = df.to_html(index=False)
    st.write(table_html, unsafe_allow_html=True)

def details(data):
    st.subheader("Details", divider='rainbow')
    with st.expander("Klik untuk secara detail"):
        for i, detail in enumerate(data, start=1):
            st.write("-----------------------------------------")
            st.write(f"{i}.")
            st.write("Name :", detail["name"])
            st.write("Description :", detail["description"])
            st.write("Method :", detail["method"])
            st.write("Evidence :", detail["evidence"])
            st.write("Url :", detail["url"])
            st.write("Confidence :", detail["confidence"])
            st.write("Risk :", detail["risk"])
            st.write("Solution :", detail["solution"])
            cweid = detail['cweid']
            st.markdown(f"CWE ID: [CWE-{cweid}](https://cwe.mitre.org/data/definitions/{cweid}.html)")
            st.write("Reference :", detail["reference"])