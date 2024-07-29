import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from handler.rulebased import klasifikasi_iso_27001
from handler.indekskor import determine_score, indekskor


def dashboard(data):
    horizontalBar(data)
    pieChart(data)
# OPTIONAL
# ======================================================================
# MUST RUN AND IMPORT THE DATABASE 'deteksiserangan.sql' in DB FOLDER
    # verticalBar(data)
# ======================================================================
    score(data)

def horizontalBar(data):
    st.subheader("Risk Category", divider='rainbow')
    risks = ['Low', 'Medium', 'High']
    total_serangan = len(data)
    high_risk_count = len([item for item in data if item['risk'] == 'High'])
    medium_risk_count = len([item for item in data if item['risk'] == 'Medium'])
    low_risk_count = len([item for item in data if item['risk'] == 'Low'])
    jumlah_serangan = [low_risk_count, medium_risk_count, high_risk_count]

    data_df = {'Risk': risks, 'Total Serangan': jumlah_serangan}
    df = pd.DataFrame(data_df)
    colors = {'Low': 'green', 'Medium': 'yellow', 'High': 'red'}
    df['Color'] = df['Risk'].map(colors)
    df = df.iloc[::-1]
  
    fig = px.bar(df, x='Total Serangan', y='Risk', orientation='h', text='Total Serangan', color='Risk',
                 color_discrete_map=colors)
   
    fig.update_layout(
        title_text=f'Total Attacks found: {total_serangan}',
        title_x=0.5,
        xaxis_title='Total Attacks'
    )
    st.plotly_chart(fig)

def pieChart(data):
    st.subheader("Attack Type", divider='rainbow')
    grouped_data = {}
    for item in data:
        nama_serangan = item['name']
        risk = item['risk']
        if nama_serangan in grouped_data:
            grouped_data[nama_serangan]['Total'] += 1
            grouped_data[nama_serangan]['Risk'] = risk
        else:
            grouped_data[nama_serangan] = {'Total': 1, 'Risk': risk}
    df = pd.DataFrame({'Attack': grouped_data.keys(), 'Total': [
                      data['Total'] for data in grouped_data.values()], 'Risk': [data['Risk'] for data in grouped_data.values()]})
    total_kategori = len(grouped_data)
    df['Persentase (%)'] = (df['Total'] / total_kategori) * 100
    fig = px.pie(df, names='Attack', values='Total', title=f'Total Attack Type: {total_kategori}',
                 labels={'Attack': 'Attack',
                         'Total': 'Total Serangan', 'Risk': 'Risk'},
                 hover_name='Attack', hover_data={'Risk': True},color_discrete_sequence=px.colors.qualitative.Plotly)
    st.plotly_chart(fig)

def verticalBar(data):
    st.subheader("CIA Clasification", divider='rainbow')

    data = klasifikasi_iso_27001(data)
    serangan_grouped = {}
    for category in ['Confidentiality', 'Integrity', 'Availability']:
        alerts = data.get(category, [])
        unique_alerts = {alert['alert']: 0 for alert in alerts}
        serangan_grouped[category] = list(unique_alerts.keys())

    trace_list = []
    x = ['Confidentiality', 'Integrity', 'Availability']
    color_palette = px.colors.qualitative.Plotly
    color_index = 0

    total_confidentiality = 0
    total_integrity = 0
    total_availability = 0

    for category in ['Confidentiality', 'Integrity', 'Availability']:
        for alert_name in serangan_grouped[category]:
            total_serangan = [
                len([item for item in data["Confidentiality"] if item['alert'] == alert_name]),
                len([item for item in data['Integrity'] if item['alert'] == alert_name]),
                len([item for item in data['Availability'] if item['alert'] == alert_name])
            ]

            total_confidentiality += total_serangan[0]
            total_integrity += total_serangan[1]
            total_availability += total_serangan[2]

            trace = go.Bar(
                name=alert_name,
                x=x,
                y=total_serangan,
                hoverinfo='text+name',
            )
            trace_list.append(trace)

    layout = go.Layout(
        barmode='stack',
        xaxis=dict(title='CIA Classification'),
        yaxis=dict(title='Total Serangan')
    )

    fig = go.Figure(data=trace_list, layout=layout)
    st.plotly_chart(fig)

def score(data):
    st.subheader("Overall Score", divider='rainbow')

    grouped_data = {}
    for item in data:
        nama_serangan = item['name']
        risk = item['risk']
        confidence = item['confidence']
        score = determine_score(item)
        if nama_serangan in grouped_data:
            grouped_data[nama_serangan]['Total'] += 1
            grouped_data[nama_serangan]['Risk'] = risk
            grouped_data[nama_serangan]['Confidence'] = confidence
            grouped_data[nama_serangan]['Score'] = score
        else:
            grouped_data[nama_serangan] = {'Total': 1, 'Risk': risk, 'Confidence': confidence, 'Score': score}

    table_data = [
        {"No": i+1, "Alert": nama, "Confidence": data['Confidence'], "Risk": data['Risk'], "Score": data['Score']}
        for i, (nama, data) in enumerate(grouped_data.items())
    ]

    df = pd.DataFrame(table_data)

    st.dataframe(df,use_container_width=True,hide_index=True)
    average_score = indekskor(data)

    def get_color(average_score):
        if average_score > 8:
            return "red"
        elif 3 < average_score <= 8:
            return "blue"
        else:
            return "green"

    color = get_color(average_score)
    st.markdown(f'<h3 style="color:{color}">Overall Score : {average_score}</h3>', unsafe_allow_html=True)