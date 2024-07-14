import streamlit as st

def owasp10(data):
    st.write("Berdasarkan serangan yang telah ditemukan, berikut adalah rangking serangan berdasarkan OWASP top 10 tahun 2021")
    unique_alerts = {}
    for item in data:
        nama_serangan = item['name']
        if nama_serangan not in unique_alerts:
            unique_alerts[nama_serangan] = item
            tags = item.get('tags', {})
            
            if 'OWASP_2021_A01' in tags:
                
                st.write(f"1. Broken Access Control: {nama_serangan}")
            if 'OWASP_2021_A02' in tags:
                
                st.write(f"2. Cryptographic Failures: {nama_serangan}")
            if 'OWASP_2021_A03' in tags:
               
                st.write(f"3. Injection : {nama_serangan}")
            if 'OWASP_2021_A04' in tags:
              
                st.write(f"4. Insecure Design: {nama_serangan}")
            if 'OWASP_2021_A05' in tags:
               
                st.write(f"5. Security Misconfiguration: {nama_serangan}")
            if 'OWASP_2021_A06' in tags:
               
                st.write(f"6. Vulnerable and Outdated Components : {nama_serangan}")
            if 'OWASP_2021_A07' in tags:
               
                st.write(f"7. Identification and Authentication Failures: {nama_serangan}")
            if 'OWASP_2021_A08' in tags:
               
                st.write(f"8. Software and Data Integrity Failures: {nama_serangan}")
            if 'OWASP_2021_A09' in tags:
               
                st.write(f"9. Security Logging and Monitoring Failures : {nama_serangan}")
            if 'OWASP_2021_A10' in tags:
               
                st.write(f"10. Server-Side Request Forgery: {nama_serangan}")