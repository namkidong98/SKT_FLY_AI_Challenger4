import os
import mysql.connector
from mysql.connector import errorcode

config={
    "host" : "kdmysql.mysql.database.azure.com",
    "user" : "kidong",
    "password" : "Pa#$.12341234",
    "database" : "db",
    "client_flags" : [mysql.connector.ClientFlag.SSL],
    "ssl_ca" : "C:\DigiCertGlobalRootCA.crt.pem" # Azure의 네트워킹에서 SSL 인증서 다운로드한 경로
}

try:
    conn = mysql.connector.connect(**config)
    print("서버에 연결됨")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("사용자나 암호가 정확하지 않습니다.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("데이터베이스가 존재하지 않습니다.")
    else:
        print(err)
