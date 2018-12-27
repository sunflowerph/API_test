#coding=UTF-8
import MySQLdb
from sshtunnel import SSHTunnelForwarder

file=open('/Users/ph/Documents/sshkey/id_rsa.rsa','r')
pd=file.read()

with SSHTunnelForwarder(
         ('120.132.11.197', 22),
         ssh_pkey='/Users/ph/Documents/sshkey/id_rsa.rsa',
         ssh_private_key_password='ph123',
         ssh_password="dy1220dy",
         ssh_username="work",
         remote_bind_address=('120.132.11.197', 22)) as server:

     conn=MySQLdb.Connect(
                host='localhost',
                port=server.local_bind_port,
                user='dev',
                passwd='dev',
                db='B2B',
                charset='utf8'
     )

# sql='show tables'
cursor=conn.cursor()
# res=cursor.execute(sql)

print conn
print cursor
conn.close()
cursor.close()