import mysql.connector
from sqlalchemy import create_engine

# MySQL Connector 설치 확인
try:
    conn = mysql.connector.connect(
        host="LocalHost",
        user="root",
        password="123456"
    )
    print("✅ mysql-connector-python 설치 확인 완료!")
    conn.close()
except Exception as e:
    print("❌ mysql-connector-python 설치 오류:", e)

# SQLAlchemy 설치 확인
try:
    engine = create_engine("mysql+mysqlconnector://root:yourpassword@localhost/test_db")
    conn = engine.connect()
    print("✅ SQLAlchemy 설치 확인 완료!")
    conn.close()
except Exception as e:
    print("❌ SQLAlchemy 설치 오류:", e)
