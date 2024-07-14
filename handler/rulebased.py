import json
import streamlit as st
from googletrans import Translator
from service.database import create_database_connection
from model.model import CIA,Alert,Relasi
from handler.url import urlShow
from handler.indekskor import determine_score

# Evaluasi dengan Prinsip-prinsip ISO/IEC 27001
def klasifikasi_iso_27001(results, print_callback=None):
    session = create_database_connection()
    c_alert = []
    i_alert = []
    a_alert = []
    for serangan in results:
        relasi = session.query(Relasi).filter_by(id_alert=serangan['alertRef']).first()
        if relasi:
            cia_entry = session.query(CIA).filter_by(id=relasi.id_cia).first()

            if cia_entry:
                if cia_entry.id == 1:
                    c_alert.append({
                        "alert": serangan["alert"],
                        "risk": serangan["risk"],
                        "evidence": serangan["evidence"],
                        "url": serangan["url"],
                        "confidence": serangan["confidence"],
                        "solution": serangan["solution"]
                    })
                elif cia_entry.id == 2:
                    i_alert.append({
                        "alert": serangan["alert"],
                        "risk": serangan["risk"],
                        "evidence": serangan["evidence"],
                        "url": serangan["url"],
                        "confidence": serangan["confidence"],
                        "solution": serangan["solution"]
                    })
                elif cia_entry.id == 3:
                    a_alert.append({
                        "alert": serangan["alert"],
                        "risk": serangan["risk"],
                        "evidence": serangan["evidence"],
                        "url": serangan["url"],
                        "confidence": serangan["confidence"],
                        "solution": serangan["solution"]
                    })
    if print_callback:
        print_callback("Total prediksi serangan ditemukan : " + str(len(results)))
        print_callback("Total serangan yang mengancam Kerahasiaan (Confidentiality) : " + str(len(c_alert)))
        print_callback("Total serangan yang mengancam Integritas (Integrity) : " + str(len(i_alert)))
        print_callback("Total serangan yang mengancam Ketersediaaan (Availability) : " + str(len(a_alert)))

    session.close()
    return {
        "Confidentiality": c_alert,
        "Integrity": i_alert,
        "Availability": a_alert,
    }

#rekomendasi
def rekomendasi(c,i,a,print_callback=None):
    def tampilkan_serangan(serangan_aspek, nama_aspek,aspek_indo):
        serangan_grouped = {}  
        translator = Translator()

        if len(serangan_aspek) > 0:
            if print_callback:
                print_callback(f"========================================================================================")
                st.subheader(f"{nama_aspek}")
                print_callback(f"Sistem anda terdapat ancaman {nama_aspek.lower()} karena ada prediksi serangan yang mengancam {aspek_indo}. Prediksi Serangan yang termasuk kedalam aspek {nama_aspek.lower()} yaitu :")
            for serangan in serangan_aspek:
                alert = serangan["alert"]
                url = serangan["url"]
                risk = serangan["risk"]  
                confidence = serangan["confidence"] 
                solution = serangan["solution"]
                if alert in serangan_grouped:
                    serangan_grouped[alert]["urls"].append(url)
                    serangan_grouped[alert]["total"] += 1
                else:
                    serangan_grouped[alert] = {
                        "urls": [url], 
                        "total": 1,
                        "risk": risk, 
                        "confidence": confidence,
                        "solution": solution}  

            for nama_alert, info_serangan in serangan_grouped.items():
                if print_callback:
                    print_callback(f"-------------------------------------------------")
                    print_callback(f"- {nama_alert}")
                    print_callback(f"  - Total: {info_serangan['total']}")
                    print_callback(f"  - URLs:")
                    urlShow(info_serangan['urls'])
                    # for url in info_serangan['urls']:
                    #     print_callback(f"    - {url}")
                    print_callback(f"  - Risk: {info_serangan['risk']}")
                    print_callback(f"  - Confidence: {info_serangan['confidence']}")
                    print_callback(f"  - Solution: {info_serangan['solution']}")
                    skor = determine_score(info_serangan)
                    print_callback(f"  - Score: {skor}")
        else:
            if print_callback:
                print_callback(f"========================================================================================")
                st.subheader(f"{nama_aspek}")
                print_callback(f"Sistem anda tidak ada ancaman terhadap {nama_aspek.lower()} ({aspek_indo})")

    tampilkan_serangan(c, "Confidentiality", "Kerahasiaan")
    tampilkan_serangan(i, "Integrity","Integritas")
    tampilkan_serangan(a, "Availability","Ketersediaan")

def rulebased(data, print_callback=None):
    hasil_klasifikasi = klasifikasi_iso_27001(data,print_callback)
    rekomendasi(hasil_klasifikasi["Confidentiality"],hasil_klasifikasi["Integrity"],hasil_klasifikasi["Availability"],print_callback)