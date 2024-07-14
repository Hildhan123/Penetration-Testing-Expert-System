import streamlit as st

def urlShow(urls):

    # Buat expander
    with st.expander("Klik untuk melihat lebih banyak"):
        # Tambahkan konten yang ingin ditampilkan dalam expander di dalam blok 
        for i, url in enumerate(urls, 1):
            st.write(f"{i}. {url}")