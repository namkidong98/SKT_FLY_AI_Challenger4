import os
import mysql.connector
from mysql.connector import errorcode

config={
    "host" : "kdmysql.mysql.database.azure.com",
    "user" : "kidong",
    "password" : "Pa#$.12341234",
    "database" : "db",
    "client_flags" : [mysql.connector.ClientFlag.SSL],
    "ssl_ca" : "C:\DigiCertGlobalRootCA.crt.pem" # 
}
conn = mysql.connector.connect(**config)

cursor = conn.cursor()

# 이미 테이블이 있다면 삭제
cursor.execute("DROP TABLE IF EXISTS book;")

# book 테이블 생성
cursor.execute("CREATE TABLE book (title VARCHAR(50), author VARCHAR(50), publisher VARCHAR(40));")
print(" book 테이블 생성 완료")

# book 테이블 변경(한글이 깨지지 않도록)
cursor.execute("ALTER TABLE db.book CONVERT TO CHARSET utf8mb4")

# 데이터 추가
cursor.execute("INSERT INTO book (title, author, publisher) VALUES (%s, %s, %s);", ("마케팅 불변의 법칙", "알 리스, 잭 트라우트", "마인드맵"))
print(cursor.rowcount, " 데이터 행이 추가됨")

cursor.execute("INSERT INTO book (title, author, publisher) VALUES (%s, %s, %s);", ("부의 미래", "앨빈 토플러", "청림"))
print(cursor.rowcount, " 데이터 행이 추가됨")

conn.commit()
cursor.close()
conn.close()