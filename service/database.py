from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_database_connection():
    db_url = 'mysql+pymysql://root:@127.0.0.1/deteksiserangan'
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

# session = create_database_connection()
# sql_query = text("SELECT * FROM cia;")
# results = session.execute(sql_query)
# for row in results:
#         print(row)
# session.close()