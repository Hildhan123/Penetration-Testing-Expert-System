## Expert System for penetration testing 
Application for testing your website using penetration testing. 
<br>
![2024-07-29 10-29-16 - Trim](https://github.com/user-attachments/assets/e085bc10-a84a-4e80-921b-87854de3e1bd)


## Tools and Libraries Used
- OWASP Zap
- Python
- Streamlit
- Numpy
- Pandas
- Matplotlib
- Plotly
- Etc

## Tutorial
1. Clone this repository and install it's requirements
2. Download and install OWASP Zap [https://www.zaproxy.org/download/]
3. Copy API from OWASP Zap setting and paste it to ../handler/pentest.py
4. run application by 'python -m streamlit run app.py'

## Optional feature (Confidentiality, Integrity, Availability (CIA) Classification)
1. Create database with name 'deteksiserangan' and import sql database from ../DB/deteksiserangan.sql
2. Uncomment this code fom ../handler/dashboard.sql
   <br>
   <img src="https://github.com/user-attachments/assets/0a749246-7963-4ef5-b48e-7203029f9b99" width="500px">
4. restart your application

## Tested
- Windows 10 and 11
- Python version 3.12.4
- Zap Proxy 2.14.0

## Big note
- To reduce your scanning time, change Owasp Zap scanning setting
- Actually you can test my scanning application before installing Owasp Zap. Just uncomment/comment my code from ../view/view.py
  <br>
  <img src="https://github.com/user-attachments/assets/fe5c304e-c887-44ca-ad16-86f986613b22" width="500px">

