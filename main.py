#!/usr/bin/python3.6m

import os
from os.path import join, dirname
from dotenv import load_dotenv

from sshtunnel import SSHTunnelForwarder


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ssh_host=os.getenv('SSH_HOST')
ssh_port=os.getenv('SSH_PORT')
username=os.getenv('SSH_LOGIN')
password=os.getenv('SSH_PASS')

server = SSHTunnelForwarder(
    (ssh_host, int(ssh_port)),
    ssh_username=username,
    ssh_password=password,
    remote_bind_address=('0.0.0.0', 3306),
    local_bind_address=('127.0.0.1', 13306)
)

server.start()

print(server.local_bind_port)  # show assigned local port
