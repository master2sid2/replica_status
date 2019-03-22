#!/usr/bin/python3.6m

import design
import sys, os, mysql.connector
from PyQt5 import QtWidgets
from dotenv import load_dotenv
from os.path import join, dirname
from sshtunnel import SSHTunnelForwarder


class ReplicationStatus(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("null")
        self.label_2.setText("null")
        self.label_3.setText("null")
        self.label_4.setText("null")

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    ssh_host = os.getenv('SSH_HOST')
    ssh_port = os.getenv('SSH_PORT')
    username = os.getenv('SSH_LOGIN')
    password = os.getenv('SSH_PASS')
    mysql_host = os.getenv('MYSQL_HOST')
    mysql_port = os.getenv('MYSQL_PORT')
    mysql_username = os.getenv('MYSQL_USER')
    mysql_password = os.getenv('MYSQL_PASS')
    mysql_db = os.getenv('MYSQL_DB')



    def createTunnel(self):
        server = SSHTunnelForwarder(
            (self.ssh_host, int(self.ssh_port)),
            ssh_username=self.username,
            ssh_password=self.password,
            remote_bind_address=('0.0.0.0', 3306),
            local_bind_address=('0.0.0.0', 13306)
        )
        server.start()

    def getStatus(self):
        print("Connect to mysql server", self.mysql_host)
        mydb = mysql.connector.connect(host=self.mysql_host,
                                       port=int(self.mysql_port),
                                       user=self.mysql_username,
                                       password=self.mysql_password)
        cursor = mydb.cursor()
        cursor.execute("show slave status")
        result = cursor.fetchall()
        result = str(result)
        result = result.split(",")
        self.label.setText(result[10])
        self.label_2.setText(result[11])
        self.label_3.setText(result[65])
        self.label_4.setText(result[79])
        cursor.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ReplicationStatus()
    window.createTunnel()
    window.getStatus()
    window.show()
    app.exec_()

if __name__ == '__main__':
   main()