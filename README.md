## Expert System for penetration testing 
Application for testing your website using penetration testing. 

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
1. Clone this repository and install its requirement
2. Download and install OWASP Zap
3. Copy API from OWASP Zap setting and paste it to ../handler/pentest.py
4. run application by 'python -m streamlit run app.py'

## Optional feature (Confidentiality, Integrity, Availability (CIA) Classification)
1. Run your database and import sql database from ../DB/deteksiserangan.sql
2. Uncomment this code fom ../handler/dashboard.sql
   ![image](https://github.com/user-attachments/assets/2c18df66-0355-4178-82f1-3a64fbaa9582)
   <img src="https://github.com/user-attachments/assets/2c18df66-0355-4178-82f1-3a64fbaa9582" width="100px">
4. restart your application

## Tested
- Windows 10 and 11
- Python version 3.12.4
- Zap Proxy 2.14.0

## Big note
- To reduce your scanning time, change Owasp Zap scanning setting
- Actually you can test my scanning application before installing Owasp Zap. Just uncomment/comment my code from ../view/view.py
  ![image](https://github.com/user-attachments/assets/fe5c304e-c887-44ca-ad16-86f986613b22 | width=100)

