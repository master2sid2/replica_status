#!/usr/bin/python3.6m

import os
import mysql.connector
from os.path import join, dirname
from dotenv import load_dotenv
from sshtunnel import SSHTunnelForwarder

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ssh_host=os.getenv('SSH_HOST')
ssh_port=os.getenv('SSH_PORT')
username=os.getenv('SSH_LOGIN')
password=os.getenv('SSH_PASS')
mysql_host=os.getenv('MYSQL_HOST')
mysql_port=os.getenv('MYSQL_PORT')
mysql_username=os.getenv('MYSQL_USER')
mysql_password=os.getenv('MYSQL_PASS')
mysql_db=os.getenv('MYSQL_DB')

def getStatus():
    print("Connect to mysql server", mysql_host)
    mydb = mysql.connector.connect(host=mysql_host,
                                   port=int(mysql_port),
                                   user=mysql_username,
                                   password=mysql_password)
    cursor = mydb.cursor()
    cursor.execute("show slave status")
    result = cursor.fetchall()
    result = str(result)
    result = result.split(",")
    print("Slave IO Running: ", result[10])
    print("Slave SQL Running: ", result[11])
    print("Error №: ", result[65])
    print("Error: ", result[66])
    print("Seconds Behind Master: ", result[79])

server = SSHTunnelForwarder(
    (ssh_host, int(ssh_port)),
    ssh_username=username,
    ssh_password=password,
    remote_bind_address=('0.0.0.0', 3306),
    local_bind_address=('0.0.0.0', 13306)
)

server.start()

print(server.local_bind_port)
getStatus()