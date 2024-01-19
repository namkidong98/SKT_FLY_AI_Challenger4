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

cursor.execute("UPDATE book SET publisher = %s WHERE title = %s;",\
               ("비즈니스 맵", "마케팅 불변의 법칙"))
print(cursor.rowcount, "행이 수정됨")

conn.commit()
cursor.close()
conn.close()