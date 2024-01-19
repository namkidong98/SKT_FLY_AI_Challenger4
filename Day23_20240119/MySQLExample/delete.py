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

cursor.execute("DELETE FROM book WHERE title = %(param1)s;", {'param1' : '부의 미래'})

print(cursor.rowcount, "개 행이 삭제됨")

conn.commit()
cursor.close()
conn.close()