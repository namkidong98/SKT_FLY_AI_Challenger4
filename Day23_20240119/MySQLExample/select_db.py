import os
import mysql.connector
from mysql.connector import errorcode

config={
    "host" : "kdmysql.mysql.database.azure.com",
    "user" : "kidong",
    "password" : "Pa#$.12341234",
    "database" : "db",
    "client_flags" : [mysql.connector.ClientFlag.SSL],
    "ssl_ca" : "C:\DigiCertGlobalRootCA.crt.pem"
}
conn = mysql.connector.connect(**config)

cursor = conn.cursor()

cursor.execute("SELECT * FROM book;")
rows = cursor.fetchall()
print(cursor.rowcount, "개의 데이터 행 검색됨")

for row in rows:
    print("데이터 행 = (%s, %s, %s)" % (str(row[0]), str(row[1]), str(row[2])))

conn.commit()
cursor.close()
conn.close()