import configparser

import mysql.connector


parser = configparser.ConfigParser()
parser.read("database.conf")
database = parser.get("mysql_config", "database")
user = parser.get("mysql_config", "username")
password = parser.get("mysql_config", "password")
host = parser.get("mysql_config", "host")
port = parser.get("mysql_config", "port")

cnx = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database,
)

cur = cnx.cursor()
cur.execute("SELECT CURDATE()")
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

cur.execute("CREATE DATABASE IF NOT EXISTS OurDB")
cur.execute("CREATE TABLE IF NOT EXISTS employees (name VARCHAR(255), address VARCHAR(255))")

sql_command = "INSERT INTO employees (name, address) VALUES ('Jazz', 'Papiyong Kook Kook')"
cur.execute(sql_command)
cnx.commit()

cur.execute("SELECT * FROM employees")
results = cur.fetchall()
for each in results:
    print(each)


cnx.close()
