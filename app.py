import streamlit as st
from view.view import render_app

def main():
    st.set_page_config(page_title="Expert System for Predicting Attacks on Websites")
    render_app()

if __name__ == "__main__":
    main()