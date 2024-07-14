import streamlit as st
from view.view import render_app

def main():
    st.set_page_config(page_title="Sistem Pakar Prediksi Serangan pada Website")
    # Panggil fungsi render_app() dari view.py
    render_app()

if __name__ == "__main__":
    main()