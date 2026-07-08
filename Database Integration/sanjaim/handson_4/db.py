import time
import mysql.connector

db_config = {
    "host" : "localhost",
    "user" : "sanjai",
    "password" : "abcdef",
    "database" : "college_dbt"
}

def get_connection():
    return mysql.connector.connect(**db_config)